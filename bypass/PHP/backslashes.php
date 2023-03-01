<?php	
	// code taken from
	// https://www.programmersought.com/article/30723400042/
	var_dump($argv);

	// vulnerable code
	eval('$str="' . addslashes($argv[1]) . '";');
	echo $str . " \n";
	
	// single vs double quotes
	$a = 1;
	echo 'a is $a' . "\n";
	echo "a is $a \n";
	echo "'a is $a'" . "\n";

	$test = "hello world!";
	function a() {
		$str = 'test';
		return $str;
	}
	echo "${a()}";

	// example payload
	// ${phpinfo()}
?>
