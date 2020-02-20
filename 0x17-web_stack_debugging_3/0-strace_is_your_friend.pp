# Fix Apache 500 error with puppet instead bash

exec { 'Fix loaded files extensions':
    command => "sudo sed -i 's/.phpp/.php/g' wp-settings.php ",
    path    => '/usr/bin',
    cwd     => '/var/www/html'
}
