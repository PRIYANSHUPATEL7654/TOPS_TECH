from filesystem_server import handle_command,ROOT
(ROOT/'sample.txt').write_text('Sample file for a restricted file service.',encoding='utf-8')
assert 'sample.txt' in handle_command('LIST')['files']
assert handle_command('GET sample.txt')['content'].startswith('Sample file')
assert handle_command('GET missing.txt')['error']=='File not found'
assert not handle_command('GET ../secret.txt')['ok']
assert handle_command('DELETE sample.txt')['ok']
print('Filesystem checks passed: list, download, not-found, traversal protection, delete.')
