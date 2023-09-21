# Can Language Models Follow Discussions ?
This is the repository for the bachelor's thesis by Nico Previtali at Hochschule Luzern on the topic: "Can Language Models Follow Discussions?"
  
## Folder Structure 
Can_Language_Models_Follow_Discussions    
│  
├── data_preparation  
│   └── kialo_data  
│       ├── 1_raw_data  
│       ├── 2_cleaned_data_JSON  
│       ├── 3_data_analysis  
│       └── 4_diagram_files  
│  
├── model_selection  
│  
├── probing  
│   ├── task_1  
│   │   ├── analysis  
│   │   └── data  
│   ├── task_2  
│   │   ├── analysis  
│   │   └── data  
│   ├── task_3  
│   │   ├── analysis  
│   │   └── data  
│   ├── task_4  
│   │   ├── analysis  
│   │   └── data  
│   └── task_5  
│       ├── analysis  
│       └── data  
│  
└── supplementary_material  
│    
├── final_interpretation    
│   ├── discussion    
│   ├── conclusion    
│   └── (recommendations)    
│    
└── supplementary_material      

  

## Auftrag (Complesis)

### Typ der Arbeit 
Bachelorarbeit (BAA)
 
### Titel
Can Language Models Follow Discussions?
 
### Ausgangslage und Problemstellung
Die Diskussion ist ein elementarer Bestandteil des Meinungsaustausches. Dies kann sowohl synchron in einem direkten Gespräch von mehreren Personen oder asynchron auf Social Media, Foren, oder Diskussions-Plattformen wie kialo.com geschehen.

Dabei haben Personen oft ein implizites Verständnis über die aktuelle Granularität und Richtung der Diskussion zu einem gewissen Zeitpunkt. Jedoch ist es unklar, inwiefern Language Model (wie BERT (Devlin et al., 2018), T5 (Raffel et al., 2020), oder UL2 (Tay et al., 2022)) diese Kompetenzen auch besitzen.

### Probing
Innerhalb dieses Projektes sollen darum die Fähigkeiten von solchen Modellen Diskussionen zu folgen erprobt werden.

#### Sourcen für Probing
Tay, Y., Dehghani, M., Tran, V. Q., Garcia, X., Bahri, D., Schuster, T., ... & Metzler, D. (2022). Unifying language learning paradigms. arXiv preprint arXiv:2205.05131.
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... & Liu, P. J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. The Journal of Machine Learning Research, 21(1), 5485-5551.

### Ziel der Arbeit und erwartete Resultate
Das Ziel dieser Arbeit ist zum einen relevanten theoretischen Hintergründe wie Rethorical Structure Theory (Mann and Thompson, 1987) oder Discourse Representation Theory (Kamp et al., 2011; Geurts and Beaver, 2007) zu erarbeiten. Darauf aufbauend sollen verschiedene Tasks definiert werden welche die nötigen Kompetenzen repräsentieren, um einer Diskussion zu folgen (z.b. betreffen zwei Aussagen das gleiche Thema). Abschliessend sollen verschiedenen aktuelle Modelle mithilfe von Probing (Tenney et al., 2019; Rogers et al., 2021) oder Prompting (Liu et al., 2023) auf diesen Tasks evaluiert werden.

### Hauptforschungsfrage
Damit soll die folgende Hauptforschungsfrage beantwortet werden, wie gut können Language Models Diskussionen folgen? Dazu werden die folgenden Unter-Forschungsfragen betrachtet:

- Welche Eigenschaften sind essenziell, um Diskussionen folgen zu können?
- Wie können diese Eigenschaften mithilfe von Probing Task innerhalb von Language Models verifiziert werden?
- Wie unterscheiden sich verschiedene Language Models auf diesen Tasks und welche ihrer Eigenschaften sind entscheidend für Unterschiede?
- Welches implizites Verständnis einer Diskussion können wir von einem Language Model erwarten?

### Erwartete Resultate
Resultierend aus dieser Arbeit werden folgende Resultate erwartet:

- Theoretische Erarbeitung von technischen (Natural Lanugage Processing, Machine Learning) und theoretischen Aspekten (welche Fähigkeiten sind nötig, um einer Diskussion zu folgen?)
- Definition von 5+ Tasks um Language Models auf diesen Fähigkeiten zu überprüfen
- Evaluation von verschiedenen Language Models anhand von diesem definierten Task
- Bericht
- Repository mit dem verwendeten Code

#### Sourcen für Linguistik
Mann, W. C., & Thompson, S. A. (1987). Rhetorical structure theory: A theory of text organization (pp. 87-190). Los Angeles: University of Southern California, Information Sciences Institute.
Geurts, B., & Beaver, D. (2007). Discourse representation theory.
Kamp, H., Van Genabith, J., & Reyle, U. (2011). Discourse representation theory. Handbook of Philosophical Logic: Volume 15, 125-394.
Tenney, I., Das, D., & Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. arXiv preprint arXiv:1905.05950.
Rogers, A., Kovaleva, O., & Rumshisky, A. (2021). A primer in BERTology: What we know about how BERT works. Transactions of the Association for Computational Linguistics, 8, 842-866.
Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Computing Surveys, 55(9), 1-35.
