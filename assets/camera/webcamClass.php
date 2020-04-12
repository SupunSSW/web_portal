<?php
class webcamClass{
        
    public function saveImageToDatabase($name, $usr){
        $imge = $name;
        $uid = $usr;
        require_once( 'connectionClass.php' );
        $mysqli=new connectionClass();

        $query="INSERT INTO `snapshots` (`id`, `image`) VALUES ('" . $uid . "', '" . $imge . "')";
        // echo $query;

        $result=  $mysqli->query($query);
        
    }   
}

?>