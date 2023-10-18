file { '/root/alx/alx-system_engineering-devops/0x0C-web_server/file.txt':
  ensure => 'present',
  mode => '666',
  content => 'server {
        add_header X-Served-By $hostname;
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name abeermosaad.tech;
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                internal;
                root /var/www/abeermosaad.tech/html;
        }

        location /redirect_me {
                return 301 https://www.linkedin.com/in/abeermosaad/;
        }

        location / {
                root /var/www/abeermosaad.tech/html;
                index index.html;
                try_files $uri $uri/ =404;
        }
}
"
}
