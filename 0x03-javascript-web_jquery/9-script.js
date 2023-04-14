// JavaScript script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
// The translation of “hello” must be display in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
// Your script must work when it is imported from the <head> tag

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', (content) => {
  $('DIV#hello').text(content.hello);
});
