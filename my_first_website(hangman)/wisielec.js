//brakuje wpisywania z pliku txt np jakiej bazy 


var proba =(Math.floor(Math.random()*63));
//var haslo =Samochody[(Math.floor(Math.random()*63))];

var Samochody =new Array(64);
Samochody[0]="Abarth"
Samochody[1]="Alfa Romeo"
Samochody[2]="Aston Martin"
Samochody[3]="Audi"
Samochody[4]="Bentley"
Samochody[5]="BMW"
Samochody[6]="Bugatti"
Samochody[7]="Cadillac"
Samochody[8]="Chevrolet"
Samochody[9]="Chrysler"
Samochody[10]="Citroen"
Samochody[11]="Dacia"
Samochody[12]="Daewoo"
Samochody[13]="Daihatsu"
Samochody[14]="Dodge"
Samochody[15]="Ferrari"
Samochody[16]="Fiat"
Samochody[17]="Ford"
Samochody[18]="FSO"
Samochody[19]="Honda"
Samochody[20]="Hummer"
Samochody[21]="Hyundai"
Samochody[22]="Infiniti"
Samochody[23]="Jaguar"
Samochody[24]="Jeep"
Samochody[25]="Kia"
Samochody[26]="Koenigsegg"
Samochody[27]="Lamborghini"
Samochody[28]="Lancia"
Samochody[29]="Land Rover"
Samochody[30]="Lexus"
Samochody[31]="Łada"
Samochody[32]="Lotus"
Samochody[33]="Lincoln"
Samochody[34]="Maserati"
Samochody[35]="Maybach"
Samochody[36]="Mazda"
Samochody[37]="McLaren"
Samochody[38]="Mercedes Benz"
Samochody[39]="MG"
Samochody[40]="Mini"
Samochody[41]="Mitsubishi"
Samochody[42]="Nissan"
Samochody[43]="Opel"
Samochody[44]="Peugeot"
Samochody[45]="Porsche"
Samochody[46]="Renault"
Samochody[47]="Rolls-Royce"
Samochody[48]="Saab"
Samochody[49]="Rover"
Samochody[50]="Seat"
Samochody[51]="Skoda"
Samochody[52]="Smart"
Samochody[53]="SsangYong"
Samochody[54]="Subaru"
Samochody[55]="Suzuki"
Samochody[56]="Syrena"
Samochody[57]="TATA"
Samochody[58]="UAZ"
Samochody[59]="Toyota"
Samochody[60]="Trabant"
Samochody[61]="Volkswagen"
Samochody[62]="Volvo"
Samochody[63]="Wartburg"


var haslo = Samochody[proba]
//var haslo = "dupa";
haslo = haslo.toUpperCase();

var dlugosc = haslo.length;
var ile_skuch =0;
var haslo1="";

var yes = new Audio("yes.wav");
var no = new Audio("no.wav");


for (i=0; i<dlugosc; i++)
{
		if (haslo.charAt(i)==" ") haslo1=haslo1+ " ";
		else haslo1 =haslo1+"-";
}




function wypisz_haslo()
{
	document.getElementById("plansza").innerHTML = haslo1;
}

window.onload = start;

var litery =new Array(35);
litery[0] = "A";
litery[1] = "Ą";
litery[2] = "B";
litery[3] = "C";
litery[4] = "Ć";
litery[5] = "D";
litery[6] = "E";
litery[7] = "Ę";
litery[8] = "F";
litery[9] = "G";
litery[10] = "H";
litery[11] = "I";
litery[12] = "J";
litery[13] = "K";
litery[14] = "L";
litery[15] = "Ł";
litery[16] = "M";
litery[17] = "N";
litery[18] = "Ń";
litery[19] = "O";
litery[20] = "Ó";
litery[21] = "P";
litery[22] = "Q";
litery[23] = "R";
litery[24] = "S";
litery[25] = "Ś";
litery[26] = "T";
litery[27] = "U";
litery[28] = "V";
litery[29] = "W";
litery[30] = "X";
litery[31] = "Y";
litery[32] = "Z";
litery[33] = "Ż";
litery[34] = "Ź";


function start()
{
		var tresc_diva ="";
		
		for (i=0; i<=34; i++)
		{
			var element ="lit" +i;
			tresc_diva= tresc_diva+ '<div class="litera" id="'+element+'">'+litery[i]+'</div>';
			if ((i+1) % 7==0) tresc_diva= tresc_diva+ '<div style="clear:both;"></div>';
		}
		
		document.getElementById("alfabet").innerHTML = tresc_diva;
		
		wypisz_haslo();

}

function start()
{
		var tresc_diva ="";
		
		for (i=0; i<=34; i++)
		{
			var element ="lit" +i;
			tresc_diva= tresc_diva+ '<div class="litera" onclick="sprawdz('+i+')" id="'+element+'">'+litery[i]+'</div>';
			if ((i+1) % 7==0) tresc_diva= tresc_diva+ '<div style="clear:both;"></div>';
		}
		
		document.getElementById("alfabet").innerHTML = tresc_diva;
		
		wypisz_haslo();
}

String.prototype.ustawZnak = function(miejsce,znak)
{
	if (miejsce > this.length -1) return this.toString();
	else return this.substr(0,miejsce)+znak+this.substr(miejsce+1);
}

function sprawdz(nr)
{
	var trafiona = false;
	
	for(i=0; i<dlugosc; i++)
	{
		if(haslo.charAt(i)==litery[nr])
		{	
			haslo1= haslo1.ustawZnak(i,litery[nr]);
			trafiona =true;
		}
	}
	
	if (trafiona== true)
	{
		yes.play();
		var element ="lit" +nr;
		document.getElementById(element).style.background="#003300";
		document.getElementById(element).style.color="#00C000";
		document.getElementById(element).style.border="3px solid #00C000";
		document.getElementById(element).style.cursor="default";
		wypisz_haslo();
	}
	
	else
	{
		no.play();
		var element ="lit" +nr;
		document.getElementById(element).style.background="#330000";
		document.getElementById(element).style.color="#C00000";
		document.getElementById(element).style.border="3px solid #C00000";
		document.getElementById(element).style.cursor="default";
		document.getElementById(element).setAttribute("onclick",";");
		
		ile_skuch++;
		var obraz = "img/s"+ile_skuch+".jpg";
		document.getElementById("szubienica").innerHTML = '<img src="'+obraz+'" alt="" />';
	}
	
	//win
	if (haslo==haslo1)
	{
		document.getElementById("alfabet").style.color="#00C000";
		document.getElementById("alfabet").innerHTML = "Tak jest! Podano prawidłowe hasło: "+ haslo+'<br/><br/><span class="reset" onclick="location.reload()" >Jeszcze raz?</span>';
	}
	
	//lose
	if (ile_skuch>=9)
	{
		document.getElementById("alfabet").style.color="#C00000";;
		document.getElementById("alfabet").innerHTML = "Przegrana! Prawidłowe hasło: "+ haslo+'<br/><br/><span class="reset" onclick="location.reload()" >Jeszcze raz?</span>';
		//document.getElementById("alfabet").innerHTML = Samochody[proba];
	}
}