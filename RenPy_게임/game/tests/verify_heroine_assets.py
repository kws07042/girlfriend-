import ast, json, re, struct, textwrap
from pathlib import Path
from types import SimpleNamespace

repo = Path(__file__).resolve().parents[3]
game = repo / 'RenPy_게임/game'
config = SimpleNamespace(basedir=str(game.parent), searchpath=[str(game)])
env = {'config': config, 'ui_camera_close_beats': ()}
registry = (game / 'ui_heroine_assets.rpy').read_text(encoding='utf-8-sig')
exec(textwrap.dedent(registry.split('init -100 python:\n', 1)[1]), env)
assert config.searchpath == [str(game), str(repo)]
def resolve(p):
    return next((Path(r) / p for r in config.searchpath if (Path(r) / p).is_file()), None)
pose = (game / 'ui_character_poses.rpy').read_text(encoding='utf-8-sig')
start = pose.index('    ui_pose_files = ')
end = pose.index('\n    def ui_pose_default', start)
exec(textwrap.dedent(pose[start:end]), env)
private = (game / 'story_week01_private.rpy').read_text(encoding='utf-8-sig')
exec(textwrap.dedent(private.split('init 35 python:\n', 1)[1]), env)
for who in ('ria', 'seoyun', 'yujin', 'jihyun'):
    env['ui_pose_files'][who].update({k: env['ui_heroine_file'](who) for k in ('daily_a', 'daily_b', 'date_a', 'date_b')})
signature = (game / 'ui_character_signature.rpy').read_text(encoding='utf-8-sig')
exec(textwrap.dedent(signature.split('init 50 python:\n', 1)[1]), env)
store = SimpleNamespace(day=1, place='office', slot='morning', chapter=1, ui_scene_key='office', ui_call_contact=None, ui_pose_context=(1, 'office', 'morning', 1), ui_poses={}, ui_pose_overrides={}, ui_pose_transitions={}, ui_pose_last_actor=None, ui_pose_version=0)
env.update(store=store, ui_pose_clock=SimpleNamespace(time=lambda: 1.0), renpy=SimpleNamespace(loadable=lambda p: resolve(p) is not None), Image=lambda p: p, ui_expression_current=lambda who: 'normal')
end = pose.index('\n    class UIPoseDissolve', start)
exec(textwrap.dedent(pose[pose.index('    def ui_pose_default'):end]), env)
expression = (game / 'ui_character_expressions.rpy').read_text(encoding='utf-8-sig')
start = expression.index('    def ui_character_static_sprite(')
end = expression.index('\n    def ui_expression_after_load', start)
exec(textwrap.dedent(expression[start:end]), env)
story = '\n'.join((game / f).read_text(encoding='utf-8-sig') for f in ('story_day01.rpy', 'story_week01.rpy', 'story_week01_private.rpy'))
codes = {'ria': ('강리아', 'ri'), 'seoyun': ('한서윤', 'sy'), 'yujin': ('차유진', 'yj'), 'jihyun': ('백지현', 'jh')}
routes = 0
for who, (kr, speaker) in codes.items():
    work = 'explaining' if who == 'ria' else 'work'
    for p, name in [('master', 'MASTER'), (work, '설명' if who == 'ria' else '업무'), ('casual', '캐주얼')]:
        for state in ('normal', 'smile', 'serious'):
            got = env['ui_character_static_sprite'](who, p, state)
            want = f'히로인/{kr}/업스케일/표정/{name}_{"serious" if state == "serious" else "default"}.png'
            assert got == want and resolve(got), (got, want)
            routes += 1
    for p, name in [('signature', '대표'), ('listening', '듣는자세')] + ([('greeting', '인사'), ('honest', '솔직한대화')] if who == 'ria' else []):
        for state in ('normal', 'smile', 'serious'):
            got = env['ui_character_static_sprite'](who, p, state)
            assert got == f'히로인/{kr}/업스케일/포즈/{name}.png' and resolve(got)
            routes += 1
    for p in ('daily_a', 'daily_b', 'date_a', 'date_b'):
        for state in ('normal', 'smile', 'serious'):
            env['ui_pose_set'](who, p)
            got = env['ui_character_static_sprite'](who, p, state)
            assert got == f'히로인/{kr}/업스케일/표정/MASTER_{"serious" if state == "serious" else "default"}.png' and resolve(got)
            routes += 1
    env['ui_pose_set'](who, None)
    for line in env['ui_signature_beats'][who]:
        assert f'{speaker} "{line}"' in story
        store._last_say_who, store._last_say_what = speaker, line
        env['ui_pose_callback']('begin')
        assert env['ui_pose_current'](who) == 'signature'
        store._last_say_who = 'dh'
        env['ui_pose_callback']('begin')
        assert env['ui_pose_current'](who) == 'signature'
        unmapped = next(x for x in re.findall(r'^\s*' + speaker + r' "(.*)"$', story, re.M) if x not in env['ui_pose_beats'][who])
        store._last_say_who, store._last_say_what = speaker, unmapped
        env['ui_pose_callback']('begin')
        assert env['ui_pose_current'](who) == env['ui_pose_default'](who)
    store._last_say_who, store._last_say_what = speaker, env['ui_signature_beats'][who][0]
    store.ui_call_contact = 'test'
    store.ui_poses[who] = 'listening'
    env['ui_pose_callback']('begin')
    assert env['ui_pose_current'](who) == 'listening'
    store.ui_call_contact = None
assert sum(len(v) for v in env['ui_pose_files'].values()) == 34
assert sum(len(set(v.values())) for v in env['ui_pose_files'].values()) == 22
assert all(resolve(p) for d in env['ui_pose_files'].values() for p in d.values())
assert not list((game / 'images/characters').rglob('*.png'))
def image_size(p):
    with resolve(p).open('rb') as f:
        header = f.read(24)
    return struct.unpack('>II', header[16:24])
env['renpy'].image_size = image_size
design = (game / 'ui_design.rpy').read_text(encoding='utf-8-sig')
start = design.index('    def ui_master_avatar_box(')
end = design.index('\n    def ui_avatar(', start)
exec(textwrap.dedent(design[start:end]), env)
for who, (kr, _) in codes.items():
    assert resolve(env['ui_heroine_file'](who)) == repo / f'히로인/{kr}/업스케일/MASTER.png'
    assert env['ui_master_avatar_box'](who) == (770, 90, 500, 500)
result = dict(expressionPoseRoutes=routes, canonicalPoseReferences=34, distinctPoseImages=22, signatureDialogueBeats=8, canonicalMasters=4, replyHold=True, nextLineReset=True, phoneExclusion=True, legacyOutfitAliases=True, runtimeDuplicates=0, playtestPerformed=False)

print('PASS', result)
