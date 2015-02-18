var port = chrome.runtime.connectNative('com.mwhooker.clitabs');
port.onMessage.addListener(function(msg) {
  console.log("Received" + msg);
});
port.onDisconnect.addListener(function() {
  console.log("Disconnected");
});

/*
port.postMessage({ text: "Hello, my_application" });

chrome.windows.getAll({populate: true}, function(windows) {
  console.log(windows);

  port.postMessage({
    text: "Hello, my_application",
    windows: windows
  });

});
*/
