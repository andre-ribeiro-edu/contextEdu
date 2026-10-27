import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# Configuração da página Streamlit
st.set_page_config(
    page_title="LC-Profiler | IA Contextualizada em Matemática e Português",
    page_icon="✏️",
    layout="wide"
)

# Nome do arquivo JSON para persistência
ARQUIVO_DADOS = "dados_contexto_aprendizagem.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, list):
                    return dados
                return []
        except Exception:
            return []
    return []

def salvar_resposta(nova_resposta):
    dados = carregar_dados()
    dados.append(nova_resposta)
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def limpar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        try:
            os.remove(ARQUIVO_DADOS)
        except Exception:
            pass

# Título da Aplicação
st.title("✏️ LC-Profiler: IA Contextualizada em Matemática e Português")
st.caption("Demonstração prática do framework **Learning Context (Liu et al., 2025)** aplicado a Fundamentos de Matemática Básica e Português")

tab1, tab2 = st.tabs(["📝 Atividade Prática (Visão do Aluno)", "📊 Dashboard do Apresentador (Visão da Turma)"])

# Definição das 7 Questões (Matemática e Português)
QUESTOES = [
    {
        "id": "q1",
        "materia": "Matemática",
        "titulo": "Questão 1 (Matemática): Adição e Subtração no Cotidiano",
        "enunciado": "João tinha R$ 45,00 em sua carteira. Ele comprou um livro por R$ 18,00 e, mais tarde, ganhou R$ 12,00 do seu pai. Com quanto dinheiro João ficou no final?",
        "opcoes": [
            "A) R$ 39,00",
            "B) R$ 51,00",
            "C) R$ 27,00",
            "D) R$ 35,00"
        ],
        "gabarito_letra": "A",
        "dicas": {
            "Narrativo": "📖 **Dica Narrativa**: Pense no fluxo do dinheiro na carteira de João. Quando ele compra o livro, o dinheiro sai da carteira (45 - 18 = 27). Quando o pai dá o presente, o dinheiro entra na carteira (27 + 12 = 39).",
            "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Monte a expressão numérica do saldo $S$: $S = 45 - 18 + 12$. Resolvendo da esquerda para a direita: $45 - 18 = 27$, depois $27 + 12 = 39$.",
            "Prático": "💡 **Dica Prática**: Passo 1: Subtraia o gasto ($45 - 18 = 27$). Passo 2: Somar o ganho ($27 + 12 = 39$). Resultado = R$ 39,00."
        }
    },
    {
        "id": "q2",
        "materia": "Matemática",
        "titulo": "Questão 2 (Matemática): Multiplicação de Quantidades",
        "enunciado": "Uma caixa de lápis de cor contém 12 unidades. Se uma escola comprou 8 caixas completas para distribuir entre os alunos, quantos lápis foram comprados ao todo?",
        "opcoes": [
            "A) 80 lápis",
            "B) 96 lápis",
            "C) 108 lápis",
            "D) 64 lápis"
        ],
        "gabarito_letra": "B",
        "dicas": {
            "Narrativo": "📖 **Dica Narrativa**: Imagine colocar 8 caixas lado a lado. Em cada uma há 12 lápis. Multiplicar é o atalho para não ter que somar 12 + 12 + 12... oito vezes consecutivas!",
            "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Trata-se do produto $12 \\times 8$. Decomponha usando a propriedade distributiva: $12 \\times 8 = (10 + 2) \\times 8 = (10 \\times 8) + (2 \\times 8) = 80 + 16 = 96$.",
            "Prático": "💡 **Dica Prática**: Cálculo direto da tabuada: $12 \\times 8 = 96$ lápis no total."
        }
    },
    {
        "id": "q3",
        "materia": "Matemática",
        "titulo": "Questão 3 (Matemática): Divisão com Resto",
        "enunciado": "Uma professora deseja dividir 35 balas igualmente entre 4 alunos. Quantas balas cada aluno receberá e quantas balas sobrarão com a professora?",
        "opcoes": [
            "A) 8 balas para cada e sobram 3 balas",
            "B) 7 balas para cada e sobram 5 balas",
            "C) 9 balas para cada e sobra 1 bala",
            "D) 8 balas para cada e sobra 1 bala"
        ],
        "gabarito_letra": "A",
        "dicas": {
            "Narrativo": "📖 **Dica Narrativa**: Imagine entregar 1 bala para cada um dos 4 alunos repetidamente. Quando cada aluno receber 8 balas, você terá distribuído 32 balas no total. Como eram 35, vão sobrar 3 balas na sua mão.",
            "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Pelo algoritmo da divisão inteira de Euclides: $35 = (4 \\times q) + r$, onde o resto $0 \\le r < 4$. Como $4 \\times 8 = 32$, temos quociente $q = 8$ e resto $r = 35 - 32 = 3$.",
            "Prático": "💡 **Dica Prática**: $35 \\div 4 = 8$ (pois $8 \\times 4 = 32$). Resto: $35 - 32 = 3$ balas."
        }
    },
    # {
    #     "id": "q4",
    #     "materia": "Matemática",
    #     "titulo": "Questão 4 (Matemática): Precedência de Operações",
    #     "enunciado": "Qual é o resultado correto da expressão numérica: **15 + 5 × 2 - 4**?",
    #     "opcoes": [
    #         "A) 36",
    #         "B) 21",
    #         "C) 25",
    #         "D) 16"
    #     ],
    #     "gabarito_letra": "B",
    #     "dicas": {
    #         "Narrativo": "📖 **Dica Narrativa**: Na matemática existe uma hierarquia importante, como uma fila de prioridade: a multiplicação sempre deve ser feita antes de somar ou subtrair!",
    #         "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Regra de precedência dos operadores: operador $\\times$ tem prioridade sobre $+$ e $-$. Logo $15 + (5 \\times 2) - 4 = 15 + 10 - 4 = 25 - 4 = 21$.",
    #         "Prático": "💡 **Dica Prática**: 1º Passo: Multiplique $5 \\times 2 = 10$. 2º Passo: Faça a soma e subtração na ordem: $15 + 10 - 4 = 21$."
    #     }
    # },
    {
        "id": "q5",
        "materia": "Português",
        "titulo": "Questão 4 (Português): Ortografia e Acentuação",
        "enunciado": "Assinale a alternativa em que **TODAS** as palavras estão acentuadas corretamente segundo as regras da língua portuguesa:",
        "opcoes": [
            "A) Árvore, café, fácil",
            "B) Arvore, cafe, facil",
            "C) Árvore, café, facil",
            "D) Arvore, café, fácil"
        ],
        "gabarito_letra": "A",
        "dicas": {
            "Narrativo": "📖 **Dica Narrativa**: Lembre-se da regra das proparoxítonas: TODAS são acentuadas (Ár-vo-re). As oxítonas terminadas em '-e' (ca-fé) e paroxítonas terminadas em '-l' (fá-cil) também recebem acento.",
            "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Classificação fonética: 1) *Árvore* $\\in$ Proparoxítonas $\\implies$ 100% acentuadas. 2) *Café* $\\in$ Oxítonas terminadas em $\\{-a, -e, -o\\} \\implies$ acentuada. 3) *Fácil* $\\in$ Paroxítonas terminadas em $L \\implies$ acentuada.",
            "Prático": "💡 **Dica Prática**: Ár-vo-re (acento na antepenúltima), ca-fé (acento na última terminada em E), fá-cil (acento na penúltima terminada em L)."
        }
    },
    # {
    #     "id": "q6",
    #     "materia": "Português",
    #     "titulo": "Questão 6 (Português): Classe de Palavras (Gramática)",
    #     "enunciado": "Na frase *'O aluno dedicado estuda diariamente'*, a palavra em destaque **estuda** pertence a qual classe gramatical?",
    #     "opcoes": [
    #         "A) Substantivo",
    #         "B) Adjetivo",
    #         "C) Verbo",
    #         "D) Advérbio"
    #     ],
    #     "gabarito_letra": "C",
    #     "dicas": {
    #         "Narrativo": "📖 **Dica Narrativa**: Os verbos são as palavras que indicam ação ou movimento. Pergunta de ouro: o que o aluno está fazendo? Ele estuda!",
    #         "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Na análise sintático-semântica: 'aluno' = sujeito (substantivo), 'dedicado' = modificador (adjetivo), 'estuda' = núcleo do predicado verbal (verbo de ação), 'diariamente' = advérbio de modo.",
    #         "Prático": "💡 **Dica Prática**: Palavra que indica ação e varia no tempo (eu estudo, ele estuda, nós estudamos) é um **Verbo**."
    #     }
    # },
    {
        "id": "q7",
        "materia": "Português",
        "titulo": "Questão 5 (Português): Pontuação e Uso da Vírgula",
        "enunciado": "Qual das frases abaixo apresenta o uso **CORRETO** da vírgula para separar elementos de uma enumeração?",
        "opcoes": [
            "A) Maria comprou cadernos lápis, borrachas e canetas.",
            "B) Maria comprou, cadernos, lápis borrachas e canetas.",
            "C) Maria comprou cadernos, lápis, borrachas e canetas.",
            "D) Maria comprou cadernos lápis borrachas, e canetas."
        ],
        "gabarito_letra": "C",
        "dicas": {
            "Narrativo": "📖 **Dica Narrativa**: Pense na vírgula como pequenas pausas enquanto você lê sua lista de compras. Antes do último item da lista, usa-se a palavra 'e' em vez da vírgula.",
            "Lógico-Matemático": "𝛴 **Dica Formal/Matemática**: Regra de sintaxe para lista de elementos $E_1, E_2, E_3 \\text{ e } E_4$. Usa-se vírgula entre termos coordenados de mesma função sintática, exceto antes da conjunção aditiva 'e'.",
            "Prático": "💡 **Dica Prática**: Separe os itens da lista por vírgulas: *cadernos, lápis, borrachas*. O último item vem com 'e': *e canetas*."
        }
    }
]

# ==========================================
# TAB 1: VISÃO DO ALUNO
# ==========================================
with tab1:
    st.subheader("1. Seu Perfil de Aprendizagem (Learning Context)")
    st.markdown("""
    Configure abaixo o seu **nome**, **preferências cognitivas** e **estado afetivo**.
    A IA utilizará este **contexto duradouro (*Who*)** para personalizar as dicas pedagógicas!
    """)

    col_nome, col_p1, col_p2 = st.columns([1.5, 2, 1.5])

    with col_nome:
        nome_aluno = st.text_input("Seu Nome:", placeholder="Ex: Maria Silva")

    with col_p1:
        perfil = st.selectbox(
            "Estilo de explicação preferido:",
            [
                "📖 Narrativo / Linguístico (Analogias do dia a dia, histórias e metáforas)",
                "𝛴 Lógico-Matemático (Expressões formais, regras de precedência, lógica estruturada)",
                "💡 Prático / Exemplos Diretos (Passo a passo objetivo e regras diretas)"
            ],
            index=0
        )

    with col_p2:
        ansiedade = st.select_slider(
            "Nível de ansiedade com testes e exercícios:",
            options=["Baixa 🟢", "Média 🟡", "Alta 🔴"],
            value="Média 🟡"
        )

    st.divider()
    st.subheader("2. Desafio Prático: Exercícios de Matemática e Português")
    st.markdown("Responda às 7 questões abaixo. Se precisar de ajuda, clique no botão **💡 Pedir Dica Adaptativa** em qualquer questão!")

    respostas_usuario = {}

    for idx, q in enumerate(QUESTOES, 1):
        st.markdown(f"### **{q['titulo']}**")
        st.write(q["enunciado"])

        resp_sel = st.radio(
            f"Sua resposta para a Questão {idx}:",
            q["opcoes"],
            index=None,
            key=f"radio_{q['id']}"
        )
        respostas_usuario[q["id"]] = resp_sel

        # Botão de Dica
        if st.button(f"💡 Pedir Dica Adaptativa para a Questão {idx}", key=f"btn_dica_{q['id']}"):
            st.info("🤖 **Tutor IA Contextualizado gerando dica baseada no seu perfil...**")

            prefixo_ansiedade = ""
            if "Alta" in ansiedade:
                prefixo_ansiedade = "🛡️ *[Suporte Afetivo]* Fique tranquilo(a)! Vamos analisar este conceito juntos, sem pressa.\n\n"

            perfil_chave = "Narrativo"
            if "Lógico" in perfil:
                perfil_chave = "Lógico-Matemático"
            elif "Prático" in perfil:
                perfil_chave = "Prático"

            dica_texto = q["dicas"].get(perfil_chave, q["dicas"]["Narrativo"])
            st.success(prefixo_ansiedade + dica_texto)

        st.divider()

    # SUBMISSÃO FINAL
    if st.button("🚀 Enviar Todas as Minhas Respostas ao Apresentador", type="primary"):
        if not nome_aluno or not nome_aluno.strip():
            st.error("⚠️ Por favor, digite seu **Nome** no início do formulário antes de enviar!")
        else:
            respondidas = [r for r in respostas_usuario.values() if r is not None]
            if len(respondidas) < len(QUESTOES):
                st.warning(f"⚠️ Você respondeu {len(respondidas)} de {len(QUESTOES)} questões. Por favor, responda a todas antes de enviar!")
            else:
                # Processar acertos
                detalhes_questoes = {}
                acertos_cnt = 0

                perfil_simples = "Narrativo"
                if "Lógico" in perfil:
                    perfil_simples = "Lógico-Matemático"
                elif "Prático" in perfil:
                    perfil_simples = "Prático"

                for q in QUESTOES:
                    qid = q["id"]
                    resp_escolhida = respostas_usuario[qid]
                    letra_escolhida = resp_escolhida[0] if resp_escolhida else ""
                    is_correta = (letra_escolhida == q["gabarito_letra"])
                    if is_correta:
                        acertos_cnt += 1

                    detalhes_questoes[qid] = {
                        "resposta": resp_escolhida,
                        "letra": letra_escolhida,
                        "correta": is_correta,
                        "gabarito": q["gabarito_letra"],
                        "materia": q["materia"]
                    }

                payload = {
                    "nome": nome_aluno.strip(),
                    "perfil": perfil_simples,
                    "ansiedade": ansiedade,
                    "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "acertos_total": acertos_cnt,
                    "porcentagem_acertos": round((acertos_cnt / len(QUESTOES)) * 100, 1),
                    "questoes": detalhes_questoes
                }

                salvar_resposta(payload)
                st.balloons()
                st.success(f"🎉 Parabéns, **{nome_aluno.strip()}**! Suas respostas foram enviadas com sucesso ({acertos_cnt}/7 acertos). Verifique o telão do apresentador!")

# ==========================================
# TAB 2: PAINEL DO APRESENTADOR (TELÃO)
# ==========================================
with tab2:
    st.subheader("📊 Métricas em Tempo Real da Turma")

    dados = carregar_dados()

    if not dados:
        st.info("Aguardando primeiras respostas dos participantes... As estatísticas aparecerão aqui assim que as pessoas enviarem pelo formulário.")
    else:
        df = pd.DataFrame(dados)

        # Tratar DataFrame defensivamente contra KeyError
        if "nome" not in df.columns:
            df["nome"] = "Anônimo"
        if "perfil" not in df.columns:
            df["perfil"] = "Narrativo"
        if "ansiedade" not in df.columns:
            df["ansiedade"] = "Média 🟡"
        if "acertos_total" not in df.columns:
            df["acertos_total"] = 0
        if "porcentagem_acertos" not in df.columns:
            df["porcentagem_acertos"] = 0.0

        # MÉTRICAS TOPO
        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Total de Alunos", len(df))

        # Perfil predominante defensivo
        if not df["perfil"].dropna().empty:
            perfil_pref = df["perfil"].mode()[0]
        else:
            perfil_pref = "N/A"
        m2.metric("Perfil Predominante", perfil_pref)

        media_acertos = df["acertos_total"].mean()
        m3.metric("Média de Acertos", f"{media_acertos:.1f} / 7")

        media_pct = df["porcentagem_acertos"].mean()
        m4.metric("Desempenho Geral", f"{media_pct:.1f}%")

        st.divider()

        # GRÁFICOS
        g1, g2 = st.columns(2)

        with g1:
            st.markdown("#### Distribuição dos Perfis de Aprendizagem (*Who*)")
            dist_perfil = df["perfil"].value_counts()
            st.bar_chart(dist_perfil)

        with g2:
            st.markdown("#### Nível de Ansiedade Declarado (*Affective State*)")
            dist_ansiedade = df["ansiedade"].value_counts()
            st.bar_chart(dist_ansiedade)

        st.divider()

        # TABELA DE DESEMPENHO POR QUESTÃO
        st.markdown("### 🎯 Desempenho Detalhado por Questão")

        estatisticas_questoes = []

        for idx, q in enumerate(QUESTOES, 1):
            qid = q["id"]
            corretas_cnt = 0
            total_respostas = 0

            for d in dados:
                qdict = d.get("questoes", {})
                if isinstance(qdict, dict) and qid in qdict:
                    total_respostas += 1
                    if qdict[qid].get("correta", False):
                        corretas_cnt += 1

            pct = (corretas_cnt / total_respostas * 100) if total_respostas > 0 else 0
            estatisticas_questoes.append({
                "Questão": f"Q{idx} ({q['materia']}) - {q['titulo'].split(': ')[1]}",
                "Matéria": q["materia"],
                "Gabarito": f"Opção {q['gabarito_letra']}",
                "Acertos": f"{corretas_cnt} / {total_respostas}",
                "Taxa de Acerto (%)": f"{pct:.1f}%"
            })

        df_q = pd.DataFrame(estatisticas_questoes)
        st.dataframe(df_q, use_container_width=True)

        st.divider()

        # LISTA DE PARTICIPANTES
        st.markdown("### 👥 Respostas dos Alunos")

        cols_exibir = ["nome", "perfil", "ansiedade", "acertos_total", "porcentagem_acertos"]
        if "data_hora" in df.columns:
            cols_exibir.append("data_hora")

        df_alunos = df[cols_exibir].copy()
        df_alunos.columns = ["Nome", "Perfil", "Ansiedade", "Acertos ( /7)", "Desempenho (%)"] + (["Data/Hora"] if "data_hora" in df.columns else [])

        st.dataframe(df_alunos, use_container_width=True)

        st.divider()

        # DEMONSTRAÇÃO DE ADAPTAÇÃO
        st.markdown("### 🔬 Demonstração ao Vivo do Artigo (Liu et al., 2025 - Vignette 1)")
        st.caption("Veja como a IA adapta a explicação do mesmo conceito de Matemática e Português com base no perfil selecionado:")

        demo_col1, demo_col2 = st.columns(2)

        with demo_col1:
            st.markdown("#### 📖 Perfil Alex (Narrativo / Linguístico)")
            st.warning("""
            **Estratégia**: Analogias do cotidiano e suporte afetivo.

            *Matemática*: *"Pense no fluxo do dinheiro na carteira de João. Quando ele compra o livro, o dinheiro sai da carteira (45 - 18 = 27). Quando ganha do pai, o dinheiro entra (27 + 12 = 39)..."*
            \n*Português*: *"Lembre-se da regra das proparoxítonas: TODAS são acentuadas (Ár-vo-re). As oxítonas em -e e paroxítonas em -l também pedem acento..."*
            """)

        with demo_col2:
            st.markdown("#### 𝛴 Perfil Blake (Lógico-Matemático / Formal)")
            st.info("""
            **Estratégia**: Expressões numéricas, teoria de conjuntos e regras gramaticais formais.

            *Matemática*: *"Monte a expressão $S = 45 - 18 + 12$. Resolvendo da esquerda para a direita: $45 - 18 = 27$, depois $27 + 12 = 39$..."*
            \n*Português*: *"Classificação fonética: 1) Árvore $\\in$ Proparoxítonas $\\implies$ 100% acentuadas. 2) Café $\\in$ Oxítonas em $\\{-a, -e, -o\\}$. 3) Fácil $\\in$ Paroxítonas em $L$..."*
            """)

    st.divider()
    if st.button("🗑️ Resetar Dados da Apresentação"):
        limpar_dados()
        st.rerun()
