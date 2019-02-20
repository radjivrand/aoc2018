<?php

$input = array(
    array("TIME" => "1518-03-19 00:02", "ID" => "647"),
    array("TIME" => "1518-03-23 00:04", "ID" => "2267"),
    array("TIME" => "1518-11-04 00:24", "awake" => FALSE),
    array("TIME" => "1518-09-17 00:04", "ID" => "509"),
    array("TIME" => "1518-09-24 00:30", "awake" => FALSE),
    array("TIME" => "1518-09-11 00:13", "awake" => FALSE),
    array("TIME" => "1518-05-24 00:29", "awake" => FALSE),
    array("TIME" => "1518-04-23 00:03", "ID" => "647"),
    array("TIME" => "1518-03-02 00:56", "awake" => FALSE),
    array("TIME" => "1518-06-03 00:17", "awake" => FALSE),
    array("TIME" => "1518-05-07 00:26", "awake" => TRUE),
    array("TIME" => "1518-09-01 00:30", "awake" => FALSE),
    array("TIME" => "1518-03-22 00:52", "awake" => FALSE),
    array("TIME" => "1518-03-28 00:04", "ID" => "2011"),
    array("TIME" => "1518-10-13 00:01", "ID" => "727"),
    array("TIME" => "1518-06-04 23:59", "ID" => "1229"),
    array("TIME" => "1518-11-16 00:59", "awake" => TRUE),
    array("TIME" => "1518-03-11 00:01", "ID" => "1091"),
    array("TIME" => "1518-03-22 00:29", "awake" => FALSE),
    array("TIME" => "1518-09-26 00:59", "awake" => TRUE),
);

array_multisort(array_column($input, 'TIME'), SORT_ASC, $input);

foreach ($input as &$value) {
  echo ($value['TIME']."</br>");
    
};

?>