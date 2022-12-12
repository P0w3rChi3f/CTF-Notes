# Objective: Level 3 - Getting Squirrely

## Q1 - ITS FOR NUTS - ANSWERED BY YOU NOW 2 POINTS
Visit http://mail.wey-tech.com/src/login.php to find the application number.

## Q2 - GIMME THE INFO - ANSWERED BY YOU NOW 3 POINTS
What is the PHP version number being used by the web service?

Tried robots.txt but got an error with php and apache info

	SOLUTION
nikto -h http://mail.wey-tech.com
Nikto reveals http://mail.wey-tech.com/phpinfo.php

```Nikto Output
+ Server: Apache/2.4.10 (Win32) OpenSSL/1.0.1h PHP/5.4.31
+ Retrieved x-powered-by header: PHP/5.4.31
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: src/login.php
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3233: /phpinfo.php: Contains PHP configuration information
+ Server leaks inodes via ETags, header found with file /doc/, fields: 0xd28 0x4660e277e3340 
+ OSVDB-48: /doc/: The /doc/ directory is browsable. This may be /usr/doc.
+ OSVDB-12184: /index.php?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-3092: /readme: This might be interesting...
+ OSVDB-3268: /icons/: Directory indexing found.
+ Cookie SQMSESSID created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ OSVDB-3092: /README: README file found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 13 item(s) reported on remote host
+ End Time:           2022-11-26 19:27:40 (GMT0) (142 seconds)


```

## Q3 - SQUIRREL YOUR WAY IN 7 POINTS
Gaining authenticated access to the email service via the webmail interface could prove to be useful later. Gain access, and submit the flag found within