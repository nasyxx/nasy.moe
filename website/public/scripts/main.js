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

var _done = "N"

const app = Elm.Main.embed(
    document.getElementById("container"),
    Object.assign({
            "username": "",
            "password": "",
            "port_": ""
        },
        document.location))

app.ports.set_title.subscribe(function (title) {
    document.title = title
    normal_title = document.title
    if (_done == "N") {
        _done = "Y"
        setTimeout(function () {
            domready(
                add_icon(),
                // formattime(),
                hljs.initHighlighting(),
                remove_last_tag_c(),
                remove_duplicate_h1()
            )
        }, 1000);
    }
})


app.ports.up2top.subscribe(function (_) {
    var high = window.scrollY
    if (high / 100 > 100) {
        scroll_to(0)
    } else {
        scroll_to(0)
    }
})

app.ports.init_comment.subscribe(function (_) {
    const gitalk = new Gitalk({
        clientID: '434498d156d6042c22a4',
        clientSecret: '11c8c6cce2e0c5e23749c0602841c855293476b7',
        repo: 'comments',
        owner: 'nasyxx',
        admin: ['nasyxx'],
        id: "comment",
        labels: ['comment'],
        createIssueManually: true,
        enableHotKey: true,
        perPage: 10,
        // facebook-like distraction free mode
        distractionFreeMode: false,
        body: location.href
    })
    gitalk.options.id = document.title
    gitalk.render("gitalk-comment")
})

///////////////

document.addEventListener("visibilitychange", function () {
    if (document.visibilityState == 'hidden') {
        normal_title = document.title;
        document.title = "ヽ(。_°)ノ 呜！页面崩啦！";
    } else document.title = normal_title;
});

function scroll_to(to) {
    var difference = to - window.scrollY;

    if (Math.abs(difference) < 10) {
        window.scroll(window.scrollX, to)
        return
    }

    var ratio = 60;
    window.scroll(window.scrollX, (window.scrollY * ratio + to) / (ratio + 2));

    setTimeout(function () {
        scroll_to(to);
    }, 10);
}

////

function add_icon() {
    document.querySelectorAll("h1").forEach(function (e) {
        var ele_a = document.createElement("a")
        if (e.id == "") {
            e.id = e.textContent;
        }
        ele_a.href = "#" + e.id
        var ele_i = document.createElement("i")
        ele_i.className = "fas fa-star h1_icon"
        ele_a.prepend(ele_i)
        e.prepend(ele_a)
        e.classList.add("no-before")
    })
    document.querySelectorAll("h2").forEach(function (e) {
        var ele_a = document.createElement("a")
        ele_a.href = "#" + e.id
        // ele_a.className = "h2_icon"
        var ele_i = document.createElement("i")
        ele_i.className = "far fa-star h2_icon"
        ele_a.prepend(ele_i)
        e.prepend(ele_a)
        e.classList.add("no-before")
    })
    document.querySelectorAll("h3").forEach(function (e) {
        var ele_a = document.createElement("a")
        ele_a.href = "#" + e.textContent
        // ele_a.className = "h3_icon"
        var ele_i = document.createElement("i")
        ele_i.className = "far fa-star-half h3_icon"
        ele_a.prepend(ele_i)
        e.prepend(ele_a)
        e.classList.add("no-before")
    })
    document.querySelectorAll("h4").forEach(function (e) {
        var ele_a = document.createElement("a")
        ele_a.href = "#" + e.textContent
        ele_a.className = "h4_icon"
        var ele_i = document.createElement("i")
        ele_i.className = "far fa-star-half"
        ele_a.prepend(ele_i)
        e.prepend(ele_a)
        e.classList.add("no-before")
    })
    document.querySelectorAll("#content footer").forEach(function (e) {
        var ele_i = document.createElement("i")
        var ele_i2 = document.createElement("i")
        ele_i.className = "far fa-star"
        ele_i2.className = "far fa-star"
        e.prepend(ele_i)
        e.append(ele_i2)
    })
}

function remove_last(d, q) {
    d = d.querySelectorAll(q)
    e = d[d.length - 1]
    e.classList.add("last")
}

function remove_last_tag_c() {
    document.querySelectorAll(".tags-categories").forEach(function (d) {
        remove_last(d, ".tags-list-li-a")
    })
    document.querySelectorAll(".tags-tags ").forEach(function (d) {
        remove_last(d, ".tags-list-li-a")
    })
}

function remove_duplicate_h1() {
    try {
        document.querySelector("#content").removeChild(document.querySelector("#content > h1"))
    } catch {
        console.log("Not In Blog")
    }
}

// function formattime() {
//     document.querySelectorAll("time[datetime]").forEach(function (e) {
//         e.textContent = moment(e.attributes.datetime.textContent).format("ll")
//         console.log(moment(e.attributes.datetime.textContent).format("ll"))
//     })
// }

function domready() {
    // Edited from https://github.com/ded/domready v1.0.8
    var fns = [],
        listener, hack = document.documentElement.doScroll,
        loaded = (hack ? /^loaded|^c/ : /^loaded|^i|^c/).test(document.readyState)

    if (!loaded && document)
        document.addEventListener("DOMContentLoaded", listener = function () {
            document.removeEventListener("DOMContentLoaded", listener)
            loaded = 1
            while (listener = fns.shift()) listener()
        })

    return function (fn) {
        loaded ? setTimeout(fn, 0) : fns.push(fn)
    }
}


window.addEventListener('scroll', function () {
    if (location.pathname != "/") {
        now_top = pageYOffset
        h1 = document.querySelector("#blog > header > h1")
        p = document.querySelector(".blog-header > div")
        toc = document.querySelector(".toc-n")
        if (now_top >= h1.offsetTop) {
            h1.classList.add("opacity")
            p.classList.remove("hidden")
            p.classList.remove("opacity")
            toc.classList.add("opacity")

        } else {
            p.classList.add("opacity")
            p.classList.add("hidden")
            h1.classList.remove("hidden")
            h1.classList.remove("opacity")
            toc.classList.remove("opacity")
        }
    }
});
// window.addEventListener('scroll', () => {
//     // by laobubu
//     document.body.style.backgroundPositionY = -0.3 * window.scrollY + 'px'
// }, false)
