# Splunk Notes

* Task 1
  * query `Name="Linux-Sysmon" git Image="/usr/bin/git"| top limit=20 CommandLine`
  * answer `git status`

* Task 2
  * query `Name="Linux-Sysmon" git Image="/usr/bin/git" CommandLine="*" remote`
  * answer `git@github.com:elfnp3/partnerapi.git`

* Task 3
  * query `Name="Linux-Sysmon" CommandLine="docker *"`
  * answer `docker compose up`

* Task 4
  * query ``
  * answer ``

  * Task 5
  * query ``
  * answer ``

  * Task 6
  * query ``
  * answer ``

  * Task 7
  * query ``
  * answer ``

  * Task 8
  * query ``
  * answer ``