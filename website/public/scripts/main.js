/**
 * Excited without bugs, have fun ("▔□▔)/hi~♡ Nasy.
 * -----------------------------------------------
 * |
 * |             *         *
 * |                  .                .
 * |           .
 * |     *                      ,
 * |                   .
 * |
 * |                               *
 * |          |\___/|
 * |          )    -(             .              '
 * |         =\  -  /=
 * |           )===(       *
 * |          /   - \
 * |          |-    |
 * |         /   -   \     0.|.0
 * |  NASY___\__( (__/_____(\=/)__+1s____________
 * |  ______|____) )______|______|______|______|_
 * |  ___|______( (____|______|______|______|____
 * |  ______|____\_|______|______|______|______|_
 * |  ___|______|______|______|______|______|____
 * |  ______|______|______|______|______|______|_
 * |  ___|______|______|______|______|______|____
 *
 * -----------------------------------------------
 * Author: Nasy https://nasy.moe <Nasy>
 * Date:   Mar 6, 2018
 * Email:  echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
 * Filename: main.js
 * Last modified by:   Nasy
 * Last modified time: Mar 6, 2018
 * License: MIT
 */
var normal_title = document.title

const app = Elm.Main.fullscreen(Object.assign({
        "username": "",
        "password": "",
        "port_": ""
    },
    document.location))

app.ports.set_title.subscribe(function (title) {
    document.title = title
    normal_title = document.title
})


app.ports.up2top.subscribe(function (_) {
    var high = document.body.scrollTop
    if (high / 100 > 100) {
        scroll_to(document.body, 0)
    } else {
        scroll_to(document.body, 0)
    }
})


document.addEventListener("visibilitychange", function () {
    if (document.visibilityState == 'hidden') {
        normal_title = document.title;
        document.title = "ヽ(。_°)ノ 呜！页面崩啦！";
    } else document.title = normal_title;
});

function scroll_to(element, to) {
    var difference = to - element.scrollTop;

    if (Math.abs(difference) < 10) {
        element.scrollTop = to;
        return;
    }

    var ratio = 60;
    element.scrollTop = (element.scrollTop * ratio + to) / (ratio + 2);

    setTimeout(function () {
        scroll_to(element, to);
    }, 10);
}
