<?php

$res = array();

$number = array();

for($i=0;$i<100;$i++){
    array_push($number,$i);
}



$current = 0;

for ($turns = 0; $turns < 4;$turns++){





    for ($player=0; $player < 9; $player++) {
        
        array_splice($res, $current+1,0,$number[0]);
        $current = $number[0];
//        array_push($res, $number[0]);
        array_shift($number);
        foreach ($res as $value){
            echo $value." ";
        }
        
        echo ", current: ".$current."<br>";
    }

}


?>