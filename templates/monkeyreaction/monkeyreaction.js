let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');
let canvas_parent = document.querySelector('.canvas-parent')

let parent_height = canvas_parent.clientHeight;
let parent_width = canvas_parent.clientWidth;

canvas.height = parent_height;
canvas.width = parent.width;

context.textAlign = "center";
context.textBaseline = "middle";
context.fillText('Click in this area', canvas.height / 2, canvas.width / 2);

let start = document.getElementById('start');
let time_text = document.getElementById('time-text');

let GameStatus = {
    STOP: 1,
    START: 2,
}

let status = GameStatus.STOP;

function end_game(){

}

function start_game() {

}

start.addEventListener('click', function() {
    if (status === GameStatus.START){
        end_game();
    }else{
        start_game();
        this.innerHTML = "Stop Game";
    }
});