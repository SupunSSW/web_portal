<?php
class connectionClass extends mysqli{
    public $host="localhost",$dbname="nbdatabase",$dbpass="",$dbuser="root";
    public $con;
    
    public function __construct() {
        $this->con= $this->connect($this->host, $this->dbuser, $this->dbpass, $this->dbname);
        
    }
}

?>