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

$string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$st = array();

foreach (str_split($string) as $key => $value) {
    //    echo("jes: ".$value."</br>");

    $before = "";
    $after = "";
    foreach ($input as $k => $v) {
        if ($v[1] == $value) {
            $before .= $v[0];
            $st[$value]["before"] .=$v[0];
        }

        if ($v[0]==$value) {
            $after .= $v[1];
            $st[$value]["after"] .=$v[1];
        }
    }

    if($before == "") {
        $start .= $value;
        //        echo $start   ;
    }

    if($after == "") {
        $stop .= $value;
    }

    echo ($before." : ".$value." : ".$after."</br>");
}
echo ("start: ".$start.", stop: ".$stop."</br>");

//print_r($st);

echo ("</br></br></br>");

$next = str_split($start);
asort($next);

$result = array();


for ($i=0;$i<1;$i++){
    $holder = $next[0];
    foreach (str_split($st[$holder]["after"]) as $key => $value){



        array_push($next,$value);
        print_r($next);
        echo ("</br>");



        asort($next);
        $next = array_values($next);


    }

    array_push($result,$holder);
    print_r($result);
    echo ("</br></br>");


    array_shift($next);
    print_r($next);
    echo ("</br></br>");




}




print_r($result);
print_r($next);





//$result = array();
//
//foreach(str_split($start) as $vstart){
//    foreach(str_split($st[$vstart]["after"]) as $value) {
//        foreach(str_split( $st[$value]["after"]) as $v){
//            foreach(str_split( $st[$v]["after"]) as $v2){
//                foreach(str_split( $st[$v2]["after"]) as $v3){
//                    foreach(str_split( $st[$v3]["after"]) as $v4){
//                        foreach(str_split( $st[$v4]["after"]) as $v5){
//                            foreach(str_split( $st[$v5]["after"]) as $v6){
//                                foreach(str_split( $st[$v6]["after"]) as $v7){
//                                    foreach(str_split( $st[$v7]["after"]) as $v8){
//                                        foreach(str_split( $st[$v8]["after"]) as $v9){
//                                            foreach(str_split( $st[$v9]["after"]) as $v10){
//                                                array_push($result, $vstart.$value.$v.$v2.$v3.$v4.$v5.$v6.$v7.$v8.$v9.$v10);
//                                            }
//                                        }
//                                    }
//                                }
//                            }
//                        }
//                    }
//                }
//            }
//        }
//    }
//}
//
//asort($result);
//
//print_r($result);
//


//$new_res = array();
//
//
//foreach ($result as $key => &$value) {
//    $new_res[$key]["pikkus"] = strlen($value);
//    $new_res[$key]["string"] = $value;
//
////    echo("string: ".$value.", pikkus: ".strlen($value)."</br>");
//    
//}
//
//
//function cmp($a, $b)
//{
//    return strcmp($b["pikkus"], $a["pikkus"]);
//}
//
//usort($new_res, "cmp");
//
//
//foreach($new_res as $value){
//    echo($value["string"]."</br>");
//    
//}


?>