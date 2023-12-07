document.addEventListener('DOMContentLoaded', function () {
    var clipboard = new ClipboardJS('#copyButton');

    clipboard.on('success', function (e) {
        console.log('Text copied to clipboard:', e.text);
        e.clearSelection();
    });

    clipboard.on('error', function (e) {
        console.error('Unable to copy text to clipboard:', e.action);
    });
});
