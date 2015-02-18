var port = chrome.runtime.connectNative('com.mwhooker.clitabs');

function getTabs(uuid) {
  chrome.windows.getAll({populate: true}, function(windows) {
    console.log(windows);
    port.postMessage({
      _id: uuid,
      windows: windows
    });
  });
}

var handlers = {
  'index': getTabs
};

port.onMessage.addListener(function(msg) {
  if (!_.has(msg, 'command')) {
    console.log('malformed message.');
    return
  }
  if (!_.has(handlers, msg['command'])) {
    console.log("don't know what to do with command " + msg['command']);
    return
  } 
  var handler = handlers[msg['command']];
  handler(msg['_id']);
});

port.onDisconnect.addListener(function() {
  console.log("Disconnected");
});
