# clitabs

interact with chrome's tabs over the command line

## install

* need to copy com.mwhooker.clitabs to ~/Library/Application Support/Google/Chrome/NativeMessagingHosts


## examples

```
$ ctabs cat
https://google.com
https://developer.chrome.com/extensions/nativeMessaging
http://en.wikipedia.org/wiki/Telomerase_reverse_transcriptase
chrome://extensions/

http://research.culturalequity.org/rc-b2/get-audio-ix.do?ix=recording&id=749&idType=performerId&sortBy=abc
http://en.wikipedia.org/wiki/Minnesota_Starvation_Experiment
http://en.wikipedia.org/wiki/The_Old_Man_of_Lochnagar

$ ctabs cat | grep -v wiki | ctabs
$ ctabs cat
https://google.com
https://developer.chrome.com/extensions/nativeMessaging
chrome://extensions/

http://research.culturalequity.org/rc-b2/get-audio-ix.do?ix=recording&id=749&idType=performerId&sortBy=abc
```
