<?php

ini_set('max_execution_time', 300);

$input = file_get_contents('./input.txt', FILE_USE_INCLUDE_PATH);

$test_input = "dabAcCaCBAcCcaDA";




function react ($in_arr) {

    $arr = str_split($in_arr);


    $arr_1 = array();
    $arr_1[count($arr_1)] = $arr[0];
    array_shift($arr);

    while (count($arr) > 0) {

        $a = $arr_1[count($arr_1)-1];

        if (  (strtoupper($a) != $a && strtoupper($a) == $arr[0])    || (strtolower($a) != $a && strtolower($a) == $arr[0]) ) {

            //        echo ("1: ".$arr_1[count($arr_1)-1].", 2: ".$arr[0].", arr_length: ".count($arr)."</br>");

            array_pop($arr_1);
            array_shift($arr);

        } else {

            $arr_1[count($arr_1)] = $arr[0];
            array_shift($arr);


        }

    }

    return (count($arr_1));
}



//echo (react($input));


for ($i=65;$i<90;$i++) 
{
    //    echo(chr($i));
    //    echo(chr($i+32));
    $pattern = '/'.chr($i).'|'.chr($i+32).'/';
    $replacement = '';
    $new_string = preg_replace($pattern, $replacement, $input);
    
    
    echo (chr($i).": ".react($new_string)."</br>");

}




//10133

?>