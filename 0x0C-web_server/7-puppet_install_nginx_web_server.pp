<<<<<<< HEAD
# Automating project requirements using Puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/Saint8083 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

=======
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin
        stats timeout 30s
        user haproxy
        group haproxy
        daemon
        
        # New commands
        maxconn 2048
        tune.ssl.default-dh-param 2048

        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private

        # See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.0.3&config=intermediate
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        
	# New commands
        option forwardfor
        option http-server-close

frontend ernestampene_front_end
    bind *:80
    bind *:443 ssl crt /etc/haproxy/certs/www.besthor.tech.pem
    http-request redirect scheme https unless { ssl_fc }
    http-request set-header X-Forwarded-Proto https
    default_backend ernestampene_back_end

backend ernestampene_back_end
    balance roundrobin
    
    server 223589-web-02 52.5.126.226:80 check
    server 223589-web-02 54.236.56.6:80  check

backend letsencrypt-backend
    server letsencrypt 127.0.0.1:54321
>>>>>>> 4c723189aa7c1172804613cf812a279264384928
