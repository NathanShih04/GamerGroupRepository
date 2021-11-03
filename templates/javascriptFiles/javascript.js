let btn = document.getElementById('btn');
let output = document.getElementById('output');
let websites =
    [
        'Ocean Conservancy - https://oceanconservancy.org/',
        'The Bay Foundation - https://www.santamonicabay.org/who-we-are/mission-and-history/',
        'BlueVoice - https://www.bluevoice.org/',
        'Billion Oyster Project - https://www.billionoysterproject.org/',
        'Conservation International - https://www.conservation.org/home',
        'Coral Reef Alliance - https://coral.org/en/',
        'Coral Restoration Foundation - https://www.coralrestoration.org/',
        'GreenWave - https://www.greenwave.org/',
        'Marine Conservation Institute - https://marine-conservation.org/',
        'Marine Fish Conservation Network - https://conservefish.org/',
        'Mission Blue - https://mission-blue.org/about/',
        'Monterey Bay Aquarium - https://www.montereybayaquarium.org/',
        'Oceana - https://oceana.org/',
        'SeaSave Foundation - https://seasave.org/',
        'Sea Shepherd - https://seashepherd.org/',
        'The Ocean Project - https://theoceanproject.org/',
        'Oceanic Global - https://oceanic.global/',
        'Reef Relief - https://www.reefrelief.org/',
        'Sea Turtle Conservancy - https://conserveturtles.org/'
    ];

btn.addEventListener('click', function(){
    var randomWebsite = websites[Math.floor(Math.random() * websites.length)]
    output.innerHTML = randomWebsite;
})
