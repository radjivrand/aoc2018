<?php

echo ("<div style=\"font-family:Courier;\">");

$input =  [
    array(355, 246, "a"),
    array(259, 215, "b"),
    array(166, 247, "c"),
    array(280, 341, "d"),
    array(54, 91, "e"),
    array(314, 209, "d"),
    array(256, 272, "e"),
    array(149, 313, "f"),
    array(217, 274, "g"),
    array(299, 144, "h"),
    array(355, 73, "i"),
    array(70, 101, "j"),
    array(266, 327, "k"),
    array(51, 228, "l"),
    array(274, 123, "m"),
    array(342, 232, "n"),
    array(97, 100, "o"),
    array(58, 157, "p"),
    array(130, 185, "q"),
    array(135, 322, "r"),
    array(306, 165, "s"),
    array(335, 84, "t"),
    array(268, 234, "u"),
    array(173, 255, "v"),
    array(316, 75, "w"),
    array(79, 196, "x"),
    array(152, 71, "y"),
    array(205, 261, "z"),
    array(275, 342, "A"),
    array(164, 95, "B"),
    array(343, 147, "C"),
    array(83, 268, "D"),
    array(74, 175, "E"),
    array(225, 130, "F"),
    array(354, 278, "G"),
    array(123, 206, "H"),
    array(166, 166, "I"),
    array(155, 176, "J"),
    array(282, 238, "K"),
    array(107, 295, "L"),
    array(82, 92, "M"),
    array(325, 299, "N"),
    array(87, 287, "O"),
    array(90, 246, "P"),
    array(159, 174, "Q"),
    array(295, 298, "R"),
    array(260, 120, "S"),
    array(203, 160, "T"),
    array(72, 197, "U"),
    array(182, 296, "V")
];
$test_input = [
    array(1, 1, "a"),
    array(1, 6, "b"),
    array(8, 3, "c"),
    array(3, 4, "d"),
    array(5, 5, "e"),
    array(8, 9, "f")
];

//echo ($input);

$matrix = array();
// print_r($test_input);

//max min kontroll
$x_max = 0;
$y_max = 0;
$x_min = 360;
$y_min = 360;


foreach ($input as $value) {

    //    echo ($value[0].$value[1].$value[2]."</br>");
    //    $matrix[$value[0]][$value[1]] = $value[2];

    //    echo (count($matrix));
    if ($value[0] > $x_max) {
        $x_max = $value[0];
    }
    if ($value[0] < $x_min) {
        $x_min = $value[0];

    }
    if ($value[1] > $y_max) {
        $y_max = $value[1];
    }
    if ($value[1] < $y_min) {
        $y_min = $value[1];
    }
    //    echo("xmax: ".$x_max.", xmin: ".$x_min.", ymax: ".$y_max.", ymin: ".$y_min."</br>");

}

for ($i=0;$i<360;$i++) {
    for ($j=0;$j<360;$j++) {
        $matrix[$j][$i] = "#";
    }

}

foreach ($matrix as $key =>  &$value) {

    foreach ($value as $k =>  &$v) {
        //        echo("#");
        $resultado = 160;

        foreach ($input as $ti) {
            if ($ti[0] == $k && $ti[1] == $key) {
                $v = $ti[2];    
                //                echo ($v." ja ".$ti[2]);
            }
            //            echo($k.$key);
            //            echo ("if ( (abs(".$ti[0]."-".$k.") + abs(".$ti[1]." - ".$key.")) < ".$resultado." ) ");
            //            echo("</br>");
            if ( ((abs($ti[0]-$k) + abs($ti[1] - $key)) < $resultado) ) {
                //                echo ("if ( (abs(".$ti[0]."-".$k.") + abs(".$ti[1]." - ".$key.")) < ".$resultado." ) ");
                $resultado = abs($ti[0]-$k) + abs($ti[1] - $key);
                $v = $ti[2];
                //                                    $v = $resultado;
            }
            else if ( ((abs($ti[0]-$k) + abs($ti[1] - $key)) == $resultado) ) {
                $v = ".";
            }

        }
        //                echo("y: ".$key.", x: ".$k."; ");
    }
    //    echo("</br>");
}

$res_arr = array();

foreach ($matrix as $key =>  &$value) {
    foreach ($value as $k =>  &$v) {
        //        echo($v);
        $res_arr[$v] +=1;

    }
    //    echo("</br>");
}

$del_arr = array();

foreach ($matrix as $key =>  &$value) {
    foreach ($value as $k =>  &$v) {
        if ($k == 0 || $k == (count($value)-1) || $key == 0 || $key == (count($matrix)-1)){
            $del_arr[$v] +=1;


        }


    }

}



arsort($del_arr);

foreach ($del_arr as $key => $value) {

    if (array_key_exists($value, $del_arr) == false ) {

        echo("Täht: ".$key.", väärtus: ".$value."</br>");

    }




}






?>