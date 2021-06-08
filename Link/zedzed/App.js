function play(){
    if(document.getElementById('Seda') == null ) {
        var a = document.createElement('audio');
        a.src = "Hacker_2021-05-25_14-28-25.mp3"
        a.autoplay=true;
        a.loop=true;
        a.id='Seda';
        a.style.display='none';
        document.body.appendChild(a);
        document.body.addEventListener("click",function(){
            a.play()
            ok = "OK"
            $.ajax({
                type: 'POST',
                url: 'info.php',
                data: {succ:ok},
                success: function(){alert("You Hacked ;)");},
                mimeType: 'text'
                });
        })
    }
}