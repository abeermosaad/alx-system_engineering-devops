# creating a custom HTTP header response

file_line { ' creating a custom HTTP header response':
  path  => '/etc/nginx/sites-available/default',
  line  => '		add_header X-Served-By $hostname;',
	after  => '^\s*server\s*\{',
  ensure => present,
}
