## Questão 1: Brasileirão - Série A (30 pontos)

<hr/>

<p><strong>Contexto:</strong></p>

<p>Você recebeu um arquivo com informações dos times de futebol do Campeonato Brasileiro Série A. Esse aquivo contém os nomes dos times, o ano do campeonato, a quantidade de vitórias, a quantidade de empates, a quantidade de derrotas, a quantidade de gols realizados, a quantidade de gols sofridos, a quantidade de cartões amarelos que levou e a quantidade de cartões vermelhos que levou.</p> 

<hr/>

<p><strong>Objetivo:</strong></p>

<p>Nesse contexto, faça um programa em Python que realize as seguintes operações:</p>

<ol>
  <li>Implemente um código para ler o arquivo e montar uma lista. Como os dados deverão ser estruturados nessa lista cabe a você, aluno, decidir;<br/><br/></li>
  <li>Após a criação da lista, deve-se adicionar as seguintes informações a cada time:<br/><br/></li>
  <ol type="a">
    <li>Adicionar após a quantidade de derrotas a quantidade total de pontos, considerando que uma vitória vale 3 pontos e um empate vale 1 ponto;<br/></li>
    <li>Após a quantidade de gols sofridos o saldo de gols, que é a diferença entre gols marcados e gols sofridos.<br/><br/></li>
  </ol>
  <li>Após adicionar essas informações, gere um arquivo para cada ano (utilize como base os anos existentes no arquivo de entrada, não fixe os valores), sendo que nesse arquivo os times deverão estar classificados seguindo os seguintes critérios:<br/><br/></li>
  <ol type="a">
    <li>Total de Pontos;<br/></li>
    <li>Quantidade de Vitórias;<br/></li>
    <li>Saldo de Gols;<br/></li>
    <li>Gols Marcados.<br/><br/></li>
  </ol>
  <p>Observação: salve o arquivo no seguinte formato:<br/></p>
  <ul>
    <li>A primeira linha de cada arquivo deverá conter o título dos dados que virão a partir da segunda linha. Separe os títulos por ; (ponto e vírgula);<br/></li>
    <li>A partir da segunda linha deverão vir os dados dos times (incluindo os dados calculados por vocês no item 2). Separe os dados por ; (ponto e vírgula);<br/></li>
    <li>Salve os arquivos na mesma pasta onde está o programa e o arquivo de dados original seguindo o seguinte padrão: <strong>brasileirao_NNNN.csv</strong> (onde NNNN é o ano em questão).<br/><br/></li>    
  </ul>
  <li>Em seguida o programa deverá informar os arquivos que foram criados;<br/><br/></li>
  <li>Após exibir os arquivos criados, o programa deverá solicitar o ano desejado e, a partir dessa informação, exibir a classificação do campeonato daquele ano;<br/><br/></li>  
  <li>Após exibir a classificação, o programa deverá exibir as seguintes informações:<br/><br/></li>
  <ol type="a">
    <li>O(s) time(s) que mais levaram cartões amarelos;<br/></li>
    <li>O(s) time(s) que mais levaram cartões vermelhos;<br/></li>
    <li>O(s) time(s) que fizeram a maior quantidade de gols;<br/></li>
    <li>O(s) time(s) que levaram a maior quantidade de gols.<br/><br/></li>
  </ol>
</ol>

<hr/>
