# Fix stack so that we get to 0 failed requests

exce {'sed'
    command => 'sudo sed -i 's/ULIMIT='-n 15'/ULIMIT='-n 4096'/' /etc/default/nginx'
}
exce {'restart'
    command => 'sudo service nginx restart'
}
