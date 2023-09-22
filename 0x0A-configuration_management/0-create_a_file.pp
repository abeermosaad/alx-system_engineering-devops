#Create a File in /tmp
file { '/tmp/school':
  ensure  => file,
  content => "I love Puppet\n",
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
