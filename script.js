// Encapsula el código en una función autoejecutable para evitar contaminar el ámbito global
(function() {
    // Función para dibujar el patrón generado por Turtle en el canvas
    function drawTurtlePattern() {
        var canvas = document.getElementById('turtleCanvas');
        var ctx = canvas.getContext('2d');
        
        var h = 0;
        for (var i = 0; i < 371; i++) {
            var c = hsv_to_rgb(h, 1, 1);
            h += 0.005;
            ctx.beginPath();
            ctx.strokeStyle = 'rgb(' + Math.floor(c[0] * 255) + ',' + Math.floor(c[1] * 255) + ',' + Math.floor(c[2] * 255) + ')';
            ctx.arc(canvas.width / 2, canvas.height / 2, -i * 0.68, 0, Math.PI * 2, true);
            ctx.stroke();
            ctx.closePath();
            ctx.rotate(80 * Math.PI / 180);
        }
    }

    // Función para convertir valores HSV a RGB
    function hsv_to_rgb(h, s, v) {
        var i = Math.floor(h * 6);
        var f = h * 6 - i;
        var p = v * (1 - s);
        var q = v * (1 - f * s);
        var t = v * (1 - (1 - f) * s);
        var mod = i % 6;
        var r = [v, q, p, p, t, v][mod];
        var g = [t, v, v, q, p, p][mod];
        var b = [p, p, t, v, v, q][mod];
        return [r, g, b];
    }

    // Llama a la función para dibujar el patrón Turtle cuando se cargue el contenido de la página
    document.addEventListener("DOMContentLoaded", function() {
        drawTurtlePattern();
    });
})();
