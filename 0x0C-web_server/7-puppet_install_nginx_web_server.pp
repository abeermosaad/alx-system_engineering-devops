# Configuring server with Puppet!

exec { 'update':
    path    => '/usr/bin',
    command => 'sudo apt-get update',
}

exec { 'install_nginx':
    path    => '/usr/bin',
    command => 'sudo apt-get install nginx -y',
    unless  => 'dpkg -l | grep -q nginx',
}

exec { 'allow':
    path     => '/usr/bin',
    command  => "sudo ufw allow 'Nginx HTTP'",
    provider => 'shell',
    unless   => "sudo ufw status | grep -q 'Nginx HTTP'",
}

exec { 'mk dir':
    path    => '/usr/bin',
    command => 'sudo mkdir -p /var/www/abeermosaad.tech/html',
    returns => [0, 1],
}

file { '/var/www/abeermosaad.tech/html/index.html':
    ensure  => 'present',
    content => "Hello World!\n"
}

file { '/var/www/abeermosaad.tech/html/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n"
}

exec { 'replace_nginx_config':
  command => "sudo sed -i '/^[^#]*server_name.*;/a \\ \n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=mN_jYKCTEwU&t=10s;\n\t}' /etc/nginx/sites-available/default && sudo sed -i '/^[^#]*server_name.*;/a \\ \n\tlocation /redirect_me {\n\t\treturn 301 https://www.linkedin.com/in/abeermosaad/;\n\t}' /etc/nginx/sites-available/default && sudo sed -i '/^[^#]*server_name.*;/a \\ \n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\tinternal;\n\t\troot /var/www/abeermosaad.tech/html;\n\t}' /etc/nginx/sites-available/default",
  path    => '/usr/bin',
}


service { 'nginx':
    ensure  => running,
    enable  => true,
}
