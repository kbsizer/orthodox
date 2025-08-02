<div style="text-align: right">Last updated: 2025-08-02<br>Clicking on Abakumov or Stalin now takes you to their respective Wikipedia page</div>

#  Aleksandr Solzhenitsyn, In the First Circle

## Overview (from Wikipedia)

***In the First Circle*** is a novel by Russian writer [Aleksandr Solzhenitsyn](https://en.wikipedia.org/wiki/Aleksandr_Solzhenitsyn), released in 1968. A more complete version of the book was published in English in 2009.

The novel depicts the lives of the occupants of a [sharashka](https://en.wikipedia.org/wiki/Sharashka) (a research and development bureau made of [Gulag](https://en.wikipedia.org/wiki/Gulag) inmates) located in the Moscow suburbs. This novel is highly autobiographical. Many of the prisoners ([zeks](https://en.wikipedia.org/wiki/Gulag#Terminology)) are technicians or academics who have been arrested under [Article 58](https://en.wikipedia.org/wiki/Article_58) of the [RSFSR](https://en.wikipedia.org/wiki/RSFSR) Penal Code in [Joseph Stalin](https://en.wikipedia.org/wiki/Joseph_Stalin)'s [purges](https://en.wikipedia.org/wiki/Joseph_Stalin#Purges_and_deportations) following the [Second World War](https://en.wikipedia.org/wiki/Second_World_War). Unlike inhabitants of other Gulag [labor camps](https://en.wikipedia.org/wiki/Labor_camp), the sharashka zeks were adequately fed and enjoyed good working conditions; however, if they found disfavor with the authorities, they could be instantly shipped to Siberia.

The title is an allusion to [Dante](https://en.wikipedia.org/wiki/Dante)'s [first circle](https://en.wikipedia.org/wiki/First_circle_of_hell), or [limbo](https://en.wikipedia.org/wiki/Limbo) of Hell in *[The Divine Comedy](https://en.wikipedia.org/wiki/The_Divine_Comedy)*, wherein the philosophers of Greece, and other [virtuous pagans](https://en.wikipedia.org/wiki/Virtuous_pagan), live in a walled green garden. They are unable to enter Heaven, as they were born before Christ, but enjoy a small space of relative freedom in the heart of Hell.

## Character Map

Source: [In the First Circle (Kindle)](https://read.amazon.com/?asin=B006IDG3Y0) > Cast of Characters

*Note: There are over 50 characters, so how to represent them and their relationships is a bit of a challenge*

### Marfino

```mermaid
graph TD
	%% Zeks at the Marfino Sharashka
	subgraph Zeks at Marfino sharashka
		Nerzhin(<b>Gleb Vikentievich Nerzhin</b><br>Glebka, Glebochka, Gleb Vikentich, Vikentich<br>Zek; mathematician; assigned to Acoustics Lab; interlocutor of Rubin and Sologdin; <i>the author's alter ego</i>; age 31)
		Sologdin(<b>Dmitri Aleksandrovich Sologdin</b><br>Mitya, Mityai, Dmitri Aleksandrych<br>Zek; engineer, designer; assigned to Design Office; serving second term and twelfth year of incarceration; <i>Christian</i>; age 36)
		Rubin(<b>Lev Grigorievich Rubin</b><br>Levka, Lyova, Lyovka, Lyovochka, Lyovushka<br>Zek; linguist; assigned to Acoustics Lab; <i>steadfast Communist</i>; age 36)
		Nerzhin<--->Sologdin
		Nerzhin<--->Rubin
		Rubin<--->Sologdin
		Pryanchikov(<b>Valentin Martynovich Pryanchikov</b><br>Val, Valentulya, Valentin Martynych, Pryanchik<br>Zek; engineer, radio expert; assigned to Acoustics Lab; formerly POW under the Germans; age 31; <i>childish, delights in technical work</i>)		
		Bobynin(<b>Aleksandr Yevdokimovich Bobynin</b><br>Zek; senior engineer; assigned to Number Seven Lab; age 42; <i>the man with nothing to lose is free</i>)
		Spiridon(<b>Spiridon Danilovich Yegorov</b><br>Spiridon Danilych, Danilych<br>Zek; of peasant stock; yardman; age 50)
		Abramson(<b>Grigory Borisovich Abramson</b><br>Grigory Borisych, Borisych<br>Zek; serving second consecutive term; engineer; <i>Trotskyist</i>)
	end
	Vitalievna(<b>Serafima Vitalievna</b><br>Sima, Simochka<br>Free worker at Marfino; worked alongside Gleb Nerzhin, developed amorous interest in him)
	Nerzhin	<-- tryst ---> Vitalievna  
	Nerzhina(<b>Nadezhda Ilyinichna Nerzhina</b><br>Nadya<br>Wife of Nerzhin; graduate student)
	Nerzhina <-- spouse ---> Nerzhin

	note[<b>Key Characters:</b><br>Gleb Nerzhin, Lev Rubin, Dmitri Sologdin, Innokenty Volodin, and Joseph Stalin<br><br>With the possible exception of Rubin, the unwavering Marxist, all are richer, fuller characters in the uncensored text, and the two characters who are arguably the most important, Nerzhin and Volodin, undergo the type of change that distinguishes dynamic fictional characters from static ones.]
    
	%% Color and Highlighting Directives    
    classDef green fill:#cfa,stroke:#333,stroke-width:2px;
    classDef red fill:#faa,stroke:#333,stroke-width:2px;     
    classDef grey fill:#eee,stroke:#333,stroke-width:2px;
    class note grey
    class Nerzhin,Sologdin,Rubin green
    class Stalin,Abakumov,Oskolupov,Selivanovsky,Yakonov red
```



### Soviet Leadership and Others

```mermaid
graph TD
	%% Soviet diplomat who makes the call
	Volodin(<b>Innokenty Artemievich Volodin</b><br>Ini, Ink, Inok<br>Diplomat, State Counselor Grade Two in Ministry of Foreign Affairs, equivalent in rank to a lieutenant colonel; <i>the story opens with his phone call to the U.S. Embassy</i>; age 30)
	Volodina(<b>Dotnara Petrovna Volodina</b><br>Dotty, Nara<br>Wife of Innokenty Volodin; daughter of Pyotr Makarygin)
	Volodin <-- spouse ---> Volodina
	
	%% Others
	Stalin(<b>Joseph Stalin</b><br>Iosif Vissarionovich Djugashvili<br>Soso, Koba, Iossarionych)
    click Stalin "https://en.wikipedia.org/wiki/Joseph_Stalin" "Wikipedia page for Stalin"
	Abakumov(<b>Viktor Semyonovich Abakumov</b><br>Colonel General; Minister of State Security; formerly head of SMERSH)
	click Abakumov "https://en.wikipedia.org/wiki/Viktor_Abakumov" "Wikipedia page for Abakumov"
	Stalin -.-> Abakumov
		
	%% The Troika of Liars
	subgraph Troika of Liars
		Selivanovsky(<b>Selivanovsky</b><br>Deputy Minister of State Security)
		Oskolupov(<b>Foma Guryanovich Oskolupov</b><br>Major General; head of Special Technology Department, Ministry of State Security)
		Yakonov(<b>Anton Nikolaevich Yakonov</b><br>Anton Nikolaich<br>Engineer Colonel; chief engineer, Special Technology Department; head of operations at Marfino)
	end
	Abakumov -.-> Selivanovsky
    
    Makarygin(<b>Pyotr Afanasievich Makarygin</b><br>Public prosecutor in Moscow; father of Dinera, Dotnara, and Klara)
	
	%% Color and Highlighting Directives    
    classDef green fill:#cfa,stroke:#333,stroke-width:2px;
    classDef red fill:#faa,stroke:#333,stroke-width:2px;     
    classDef grey fill:#eee,stroke:#333,stroke-width:2px;
    class note grey
    class Nerzhin,Sologdin,Rubin green
    class Stalin,Abakumov,Oskolupov,Selivanovsky,Yakonov red
```



