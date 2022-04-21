function USU_updateButtonsBy(table) {
    const ieditable = table && table.json;
    const editable =  ieditable && table.getElementsByClassName("marked")[0];
    //const v = editable ? "visible" : "hidden";
    const v = editable ? "block" : "none";
    const iv = ieditable ? "block" : "none";
    document.querySelector("input[name='insert']").style.display = iv;
    document.querySelector("input[name='update']").style.display = v;
    document.querySelector("input[name='delete']").style.display = v;
    document.querySelector("input[name='delete']").style.display = v;

    document.getElementById("form").style.display = "none";
}

function USU_getActiveRowFrom(tbl) {
    if (!tbl || !tbl.json) {
        return null;
    }
    const trs = tbl.getElementsByTagName("tr");
    var i = 0
    for (;i < trs.length; i++) {
        if (trs[i].className === "marked") {
            i--; //substract header tr
            break;
        }
    }
    return tbl.json[i];
}

function USU_getPkFrom(tbl) {
    const json = USU_getActiveRowFrom(tbl);
    return json ? json["pk"] : null;
}

function USU_toggleRowIn(tbl,row) {
    if (!tbl || typeof tbl != 'object') {
        return;
    }
    const trs = tbl.getElementsByTagName("tr");
    for (i= 0; i < trs.length; i++) {
        trs[i].className = i == row ? "marked" : "";
    }
    USU_updateButtonsBy(tbl);
}

function USU_createTableIn(el,id,data, ignoreCol,editable) {
    if (!el || !data || typeof data != 'object' || data.length == 0) {
        return;
    }
    var keys = [];
    Object.keys(data[0]).forEach(function(key){
        if (key != ignoreCol) {
            keys.push(key);
        }
    });
    const tbl=$("<table/>").attr("id",id);
    var cells = [];
    keys.forEach(function(key) {
        cells.push("<th>"+key+"</th>");
    })
    tbl.append("<tr>"+cells.join("")+"</tr>");
    for(var i=0;i<data.length;i++) {
        cells = [];
        keys.forEach(function(key) {
            cells.push("<td>"+data[i][key]+"</td>");
        })
        tbl.append("<tr>"+cells.join("")+"</tr>");
    }
    $("#"+el.id).append(tbl);
    if (editable) {
        el.lastChild.json = data;
        el.lastChild.onclick = function(e) {
           e = e || event;
           var eventEl = e.srcElement || e.target,
               isRow = function(el) {
                         return el.tagName && el.tagName.match(/tr/i) && el.firstChild.tagName.match(/td/i);
                       };

           //move up the DOM until tr is reached
           while (eventEl = eventEl.parentNode) {
               if (isRow(eventEl)) {
                   USU_toggleRowIn(el.lastChild,eventEl.rowIndex)
                  return true;
               }
           }
           return false;
       }
   }
}

function USU_show(id,data,editable) {
    const el = document.getElementById(id);
    while (el && el.lastChild) {
        el.removeChild(el.lastChild);
    }
    USU_createTableIn(el,"tbl_"+id,JSON.parse(data),"pk",editable);
    USU_updateButtonsBy(el.lastChild);
}
