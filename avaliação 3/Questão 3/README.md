## Questão 3: Análise de Log do Apache (40 pontos)

<hr/>

<p><strong>Contexto:</strong></p>

<p>A diretoria da empresa solicitou um relatório detalhado sobre o tráfego no servidor web. Além de identificar o usuário que mais acessa o sistema, eles querem entender os padrões temporais de acesso e possíveis tentativas de invasão. Você deve processar o arquivo <Strong>apache.log</Strong> para extrair essas informações.</p> 

<hr/>

<p><strong>Objetivo:</strong></p>

<p>Escreva um programa em Python que leia o arquivo de log e responda às seguintes três perguntas, imprimindo os resultados no final:</p>

<ol>
  <li><Strong>Top Cliente:</Strong> Qual endereço IP realizou o maior número de requisições?<br/><br/></li>
  <li><Strong>Pico de Tráfego:</Strong> Qual dia (Mês/Dia/Ano) teve o maior número total de requisições?<br/><br/></li>
  <li><Sterong>Dia Crítico:</Sterong> Qual dia teve o maior número de requisições com acesso negado (erros do tipo "forbidden" ou "denied")?<br/><br/></li>
</ol>

<hr/>

<p><strong>Requisitos Obrigatórios:</strong></p>

<ul>
  <li>Utilize apenas o conteúdo visto até o momento;<br/><br/></li>
  <li>Lembre-se que será necessária uma pesquisa sobre as funções FILTER(), MAP(), SORT() e funções LAMBDA;<br/><br/></li>
  <li>O uso de conteúdos não abordados em sala implicará em penalildade de 10 pontos;<br/><br/></li>
</ul>

<hr/>

<p><strong>Gabarito:</strong></p>

<p>Seu script deve chegar aos seguintes valores:</p>

<ul>
  <li><Strong>IP mais frequente:</Strong> 218.144.240.75 (1002 requisições)<br/><br/></li>
  <li><Strong>Dia com mais tráfego:</Strong> Nov 29 2005 (2121 requisições)<br/><br/></li>
  <li><Strong>Dia com mais erros:</Strong> Jul 21 2005 (289 erros)<br/><br/></li>
</ul>

<hr/>
