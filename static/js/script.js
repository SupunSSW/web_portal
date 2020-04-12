
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    // $('#navbar').classList.add('scrolled');
    $('#navbar').attr("style", "transition: .1s;box-shadow: 0 0 1.5em rgba(0,0,0,0.2) ;");

  } else {
    $('#navbar').attr("style", "display:block");

  }
}



function clrFields() {
  let x = document.getElementsByName('tinput');

  for (let i = 0; i < x.length; i++) {
    x[i].value = '';
  }
}

function noticeSubmit() {

  let topval = document.getElementById('topic').value;
  let textval = document.getElementById('textcontent').value;

  if (topval && textval) {
    let dt = $('#dpt').val();
    let aca = $('#acayear').val();
    let exp = $('#expdate').val();
    let tp = $('#topic').val();
    let con = $('#textcontent').val();
    $.post("process.php",
      {
        typ: true,
        dpt: dt,
        acayear: aca,
        expdate: exp,
        topic: tp,
        textcontent: con
      },
      function (data, status) {
        // if(status == "success") {
        // alert(data);
        // alert(status);
        $('#succarea').attr("style", "display:block");
        clrFields();


        // }
      });

  }
  else {
    alert("Please fill in all the fields!");
  }

}


function neditSubmit() {
  let dt = $('#dpt').val();
  let nid = $('#nid').text();
  let aca = $('#acayear').val();
  let exp = $('#expdate').val();
  let tp = $('#topic').val();
  let con = $('#textcontent').val();

  if (tp && con) {
    
    $.post("action.php",
      {
        typ: 'nedit',
        idn: nid,
        dpt: dt,
        acayear: aca,
        expdate: exp,
        topic: tp,
        textcontent: con
      },
      function (data, status) {
        alert('Record Submitted!');
        window.location.replace('notices.php');
      });

  }
  else {
    alert("Please fill in all the fields!");
  }

}


function inputSubmit() {

  let fname = $('#fname').val();
  let lname = $('#lname').val();
  let uindex = $('#uindex').val();
  let regno = $('#regno').val();
  let dpt = $('#dpt').val();
  let acayear = $('#acayear').val();
  // let con = $('#textcontent').val();

  if (fname && lname && regno) {
    

    $.post("process.php",
      {
        typ: false,
        fnm: fname,
        lnm: lname,
        uin: uindex,
        reg: regno,
        dt: dpt,
        aca: acayear
      },
      function (data, status) {
        $('#succarea').attr("style", "display:block");
        clrFields();
        window.location.href('../localhost:8000/');
      });

  }
  else {
    alert("Please fill in all the fields!");
  }

}


function submitEdit() {
  let fname = $('#fname').val();
  let lname = $('#lname').val();
  let uindex = $('#uindex').text();
  let regno = $('#regno').val();
  let dpt = $('#dpt').val();
  let acayear = $('#acayear').val();
  // let con = $('#textcontent').val();

  if (fname && lname && regno) {
    $.post("action.php",
      {
        typ: 'edit',
        fnm: fname,
        lnm: lname,
        uin: uindex,
        reg: regno,
        dt: dpt,
        aca: acayear
      },
      function (data, status) {
        alert('Record Submitted!');
        window.location.replace('students.php');
      });

  }
  else {
    alert("Please fill in all the fields!");
  }
}




function editItem() {
  alert('edit');
}

function removeItem() {
  alert('remove');
}
