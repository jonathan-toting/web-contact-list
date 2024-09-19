let row_selectors = document.querySelectorAll('.row_selector');
let img_container = document.querySelectorAll('.img_container');
let btn_select_del = document.querySelectorAll('.btn_select_del');
let btn_select_edt = document.querySelectorAll('.btn_select_edt');

window.onload = function () {
    img_container.forEach(_obj => {
        _obj.style.display = 'flex';
    })
    btn_select_del.forEach(_obj => {
        _obj.style.display = 'none';
    })
    btn_select_edt.forEach(_obj => {
        _obj.style.display = 'none';
    })
    document.getElementsByClassName('btn_cancel_del')[0].style.display = 'none';
    document.getElementsByClassName('btn_cancel_edt')[0].style.display = 'none';
};

document.getElementsByClassName('btn_del')[0].onclick = function() {
    if (document.getElementsByClassName('btn_cancel_edt')[0].style.display === 'none') {
        img_container.forEach(_obj => {
            _obj.style.display = 'none';
        })
        btn_select_del.forEach(_obj => {
            _obj.style.display = 'flex';
        })
        document.getElementsByClassName('btn_cancel_del')[0].style.display = 'flex';
        document.getElementsByClassName('btn_del')[0].style.display = 'none';
    }
};

document.getElementsByClassName('btn_edt')[0].onclick = function() {
    if (document.getElementsByClassName('btn_cancel_del')[0].style.display === 'none') {
        img_container.forEach(_obj => {
            _obj.style.display = 'none';
        })
        btn_select_edt.forEach(_obj => {
            _obj.style.display = 'flex';
        })
        document.getElementsByClassName('btn_cancel_edt')[0].style.display = 'flex';
        document.getElementsByClassName('btn_edt')[0].style.display = 'none';
    }
};

document.getElementsByClassName('btn_cancel_del')[0].onclick = function() {
    img_container.forEach(_obj => {
        _obj.style.display = 'flex';
    })
    btn_select_del.forEach(_obj => {
        _obj.style.display = 'none';
    })
    document.getElementsByClassName('btn_cancel_del')[0].style.display = 'none';
    document.getElementsByClassName('btn_del')[0].style.display = 'flex';
};

document.getElementsByClassName('btn_cancel_edt')[0].onclick = function() {
    img_container.forEach(_obj => {
        _obj.style.display = 'flex';
    })
    btn_select_edt.forEach(_obj => {
        _obj.style.display = 'none';
    })
    document.getElementsByClassName('btn_cancel_edt')[0].style.display = 'none';
    document.getElementsByClassName('btn_edt')[0].style.display = 'flex';
};