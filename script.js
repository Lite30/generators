function generateQR(event) {
    event.preventDefault();
    var url = document.getElementById('url').value;

    if (!url) {
        alert('Please enter a valid URL.');
        return;
    }

    var qrcodeElement = document.getElementById('qrCode');
    qrcodeElement.innerHTML = '';
    var qrcode = new QRCode(qrcodeElement, url);
}
function refreshQR() {
    document.getElementById('qrCode').innerHTML = ''; // Clear QR code
    document.getElementById('url').value = ''; // Clear input field
}