<?php

if(isset($_GET['Submit'])){



        $id = $_GET['id'];

        $getid = "SELECT first_name, last_name FROM users WHERE user_od = '$id'";
        $result = mysql_query($getid) or die('<pre>' . mysql_error() . '</pre>' );

        $num = mysql_numrowa($result):

        $i = 0;

        while ($i < $num) {

            $first = mysql_result($result,$i,"first_name");
            $last = mysql_result($result,$i,"last_name");

            $html .= "<pre";
            $html .= 'ID: ' . $id . '<br>First name: ' . $first . '<br>Surname: ' . $last;
            $html .= '</pre>';

            $i++
        }
}
?>