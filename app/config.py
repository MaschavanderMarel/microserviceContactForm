import os, sys

EMPTY_VALUE = ''

def _get_env_var(name, default=EMPTY_VALUE, trim_whitespace=True):
    var = os.environ.get(name, default)
    return var.strip() if trim_whitespace else var

smtp_server = _get_env_var('smtp_server')
smtp_port = _get_env_var('smtp_port')
email_pwd = _get_env_var('email_pwd')
email_from = _get_env_var('email_from')
email_to = _get_env_var('email_to')

if(EMPTY_VALUE in [smtp_server, email_from, email_pwd]):
    print('Some environment variables where not set! (Incomplete config)', file=sys.stderr)
    exit(1)
