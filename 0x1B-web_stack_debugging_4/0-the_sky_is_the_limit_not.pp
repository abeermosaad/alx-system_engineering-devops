# Fix stack so that we get to 0 failed requests

exec { 'sed':
  provider => 'shell',
  command  => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  before   => Exec['restart'],
}

exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart',
}
