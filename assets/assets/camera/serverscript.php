<?php
    require_once './webcamClass.php';
                // echo "Hello I ran in Backgroud! Huuuu:-)";
                // require_once './webcamClass.php';
                // $webcamClass=new webcamClass();
                // echo $webcamClass->showImage();
                // echo print_r($_FILES['webcam']['name']);

    // if(@$_GET['Req'] == true) {
    //     echo $_GET['Req'];
    // }

                // $imageName = time() . '_' . $_FILES['webcam']['name'];
    $imageName = date('is').".jpg";
                // $filename = $_FILES['webcam']['name'];
    $target = '/opt/lampp/htdocs/nb-web-app/webcamImage/' . $imageName;
    move_uploaded_file($_FILES['webcam']['tmp_name'], $target);

    $webcamClass=new webcamClass();
    $webcamClass->saveImageToDatabase($imageName,$_GET['Req']);
?>