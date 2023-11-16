# limits_conf.pp

file { '/etc/security/limits.conf':
  ensure  => present,
  content => "holberton hard nofile 65536\nholberton soft nofile 65536\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
