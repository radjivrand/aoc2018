<?php
echo ("<div style=\"font-family:Courier;\">");

$input = [
    array("P", "F"),
    array("F", "M"),
    array("Q", "S"),
    array("K", "G"),
    array("W", "X"),
    array("V", "I"),
    array("S", "Y"),
    array("U", "D"),
    array("J", "B"),
    array("Z", "C"),
    array("Y", "D"),
    array("X", "A"),
    array("E", "N"),
    array("M", "B"),
    array("N", "I"),
    array("I", "T"),
    array("H", "A"),
    array("A", "B"),
    array("O", "L"),
    array("T", "L"),
    array("D", "R"),
    array("G", "L"),
    array("C", "R"),
    array("R", "L"),
    array("L", "B"),
    array("O", "R"),
    array("Q", "I"),
    array("M", "L"),
    array("R", "B"),
    array("J", "O"),
    array("O", "B"),
    array("Y", "L"),
    array("G", "R"),
    array("P", "Z"),
    array("K", "Y"),
    array("X", "I"),
    array("E", "H"),
    array("I", "H"),
    array("P", "K"),
    array("G", "B"),
    array("H", "L"),
    array("X", "C"),
    array("P", "X"),
    array("X", "M"),
    array("Q", "H"),
    array("S", "Z"),
    array("C", "B"),
    array("N", "A"),
    array("M", "R"),
    array("X", "E"),
    array("P", "L"),
    array("H", "G"),
    array("E", "D"),
    array("D", "L"),
    array("W", "A"),
    array("S", "X"),
    array("V", "O"),
    array("H", "B"),
    array("T", "B"),
    array("Y", "C"),
    array("A", "R"),
    array("N", "L"),
    array("V", "Z"),
    array("W", "V"),
    array("S", "M"),
    array("Z", "A"),
    array("W", "S"),
    array("Q", "R"),
    array("N", "G"),
    array("Z", "L"),
    array("K", "O"),
    array("X", "R"),
    array("V", "H"),
    array("P", "R"),
    array("M", "A"),
    array("K", "L"),
    array("P", "M"),
    array("F", "N"),
    array("W", "H"),
    array("K", "B"),
    array("H", "C"),
    array("X", "H"),
    array("V", "U"),
    array("S", "H"),
    array("J", "X"),
    array("S", "N"),
    array("V", "A"),
    array("H", "O"),
    array("Y", "O"),
    array("H", "R"),
    array("X", "T"),
    array("J", "H"),
    array("G", "C"),
    array("E", "R"),
    array("W", "J"),
    array("F", "E"),
    array("P", "I"),
    array("F", "T"),
    array("J", "L"),
    array("U", "Z"),
    array("Q", "D")
];
$test = [
    array("C", "A"),
    array("C", "F"),
    array("A", "B"),
    array("A", "D"),
    array("B", "E"),
    array("D", "E"),
    array("F", "E")
];

//$letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //GHIJKLMNOPQRSTUVWXYZ
$letters = "ABCDEF"; //GHIJKLMNOPQRSTUVWXYZ

$table = array();

//tekitab array, kus tähestik on key'deks
foreach(str_split($letters) as $key => $value) {
    $table[$value] = array("before" => array(),
                           "after" => array(),
                           "time" => array()
                          );
}

//tekitab array, kus on iga tähe arraydes kirjas, millised peavad olema enne ja millised on pärast
foreach($test as $key => $value){
    if(!in_array($table[$value[0]], $table[$value[1]]["before"])){
        array_push($table[$value[1]]["before"], $value[0]);
    }
    if(!in_array($table[$value[1]], $table[$value[0]]["after"])){
        array_push($table[$value[0]]["after"], $value[1]);
    }
}

// näitab suhete tabelit
foreach($table as $key => $value){
    echo(implode($value["before"])." < ".$key." < ".implode($value["after"]));
    echo "<br>";
    //    echo("key: ".$key.", value".$value."<br>");
}

//leiab esimese elemendi, millel pole eelkäijaid; pushib need olemasolevasse teise tabelisse
function get_free($cur_table){
    $cur_free = array();
    foreach($cur_table as $key => $value){
        if(!$value["before"]){
            array_push($cur_free,$key);
            //            return $key; //juhuks kui vaja ainult 1 välja anda
        }
    }
    return $cur_free;
}

//viskab tabelist välja määratud tähe
function remove_letter($letter, $cur_table){
    foreach($cur_table as $key => &$value){
        if ($key==$letter){
            unset($cur_table[$letter]);
        }
        $value["before"] = array_diff($value["before"],[$letter]);
        $value["after"] = array_diff($value["after"],[$letter]);
    }
    return $cur_table;
}

echo "<br><br><br>";

//$free = array();

$pipe = get_free($table);
$in_progress = array();
$action = array();

echo "<br>";

$c1=0;
$c2=0;
$flag++;

for ($i=0;$i<20;$i++){


    if (($c0 < ord($pipe[0])-64) && isset($pipe[0])){
        echo($pipe[0]);
        $c0++;
    } else {
        echo(".");
    }

    if($c0 == ord($pipe[0])-64) {
        array_push($action,$pipe[0]);
    }



    if(($c1<ord($pipe[1])-64) && isset($pipe[1])){
        echo($pipe[1]);
    } else {
        echo(".");
    }
    if($c1 == ord($pipe[1])-64) {
        array_push($action,$pipe[1]);
    }

    echo("| ".implode($action));
    
    $old_pipe = $pipe;
    foreach($action as $key => $value){
        $table = remove_letter($value, $table);
        $c0 = 0;
        $c1 = 0;
        $flag++;
    }
    
    if ($flag > 0){
        $action = array();
    }
    
    
    
    $pipe = get_free($table);

    echo "<br>";





}
















echo "<br>";
echo "<br>";

// näitab suhete tabelit
foreach($table as $key => $value){
    echo(implode($value["before"])." < ".$key." < ".implode($value["after"]));
    echo "<br>";
    //    echo("key: ".$key.", value".$value."<br>");
}



?>