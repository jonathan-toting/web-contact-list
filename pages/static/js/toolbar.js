let row_selectors = document.querySelectorAll('.row_selector');
let btn_star = document.querySelectorAll('.btn_star');
let btn_select_del = document.querySelectorAll('.btn_select_del');
let btn_select_edt = document.querySelectorAll('.btn_select_edt');

window.onload = function () {
    btn_star.forEach(_obj => {
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
        btn_star.forEach(_obj => {
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
        btn_star.forEach(_obj => {
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
    btn_star.forEach(_obj => {
        _obj.style.display = 'flex';
    })
    btn_select_del.forEach(_obj => {
        _obj.style.display = 'none';
    })
    document.getElementsByClassName('btn_cancel_del')[0].style.display = 'none';
    document.getElementsByClassName('btn_del')[0].style.display = 'flex';
};

document.getElementsByClassName('btn_cancel_edt')[0].onclick = function() {
    btn_star.forEach(_obj => {
        _obj.style.display = 'flex';
    })
    btn_select_edt.forEach(_obj => {
        _obj.style.display = 'none';
    })
    document.getElementsByClassName('btn_cancel_edt')[0].style.display = 'none';
    document.getElementsByClassName('btn_edt')[0].style.display = 'flex';
};