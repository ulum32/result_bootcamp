function is_username_valid($username){
    if(!preg_match("/^[a-z]{5,9}$/", $username)){
        return false;
    }else{
        return true;
    }
}

function is_password_valid($password){
    $uppercase = preg_match('@[A-Z]@', $password);
    $lowercase = preg_match('@[a-z]@', $password);
    $number    = preg_match('@[0-9]@', $password);
    if(!$uppercase || !$lowercase || !$number || strlen($password) < 8) {
        return false;
    }else{
        return true;
    }
}
