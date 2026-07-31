from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import unicodedata
import re
import os

from med_data import MEDICAMENTOS, ALIASES

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)


def normalizar(texto: str) -> str:
    """Remove acentos, converte para minúsculas e remove caracteres especiais."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9 ]", "", texto)
    return texto


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/buscar", methods=["GET"])
def buscar_medicamento():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"erro": "Informe o nome do medicamento."}), 400

    query_norm = normalizar(query)

    # Verifica alias primeiro
    if query_norm in ALIASES:
        query_norm = ALIASES[query_norm]

    # Busca exata
    if query_norm in MEDICAMENTOS:
        med = MEDICAMENTOS[query_norm]
        return jsonify({
            "nome_cientifico": query_norm.title(),
            "categoria": med["categoria"],
            "indicacao": med["indicacao"],
            "marcas": med["marcas"],
            "total": len(med["marcas"])
        })

    # Busca parcial (contém o termo)
    resultados_parciais = []
    for chave, med in MEDICAMENTOS.items():
        chave_norm = normalizar(chave)
        if query_norm in chave_norm or chave_norm in query_norm:
            resultados_parciais.append({
                "nome_cientifico": chave.title(),
                "categoria": med["categoria"],
                "indicacao": med["indicacao"],
                "marcas": med["marcas"],
                "total": len(med["marcas"])
            })

    if resultados_parciais:
        if len(resultados_parciais) == 1:
            return jsonify(resultados_parciais[0])
        return jsonify({"multiplos": resultados_parciais})

    return jsonify({"erro": f"Nenhum medicamento encontrado para '{query}'. Verifique o nome científico."}), 404


@app.route("/api/lista", methods=["GET"])
def listar_medicamentos():
    """Retorna todos os nomes científicos disponíveis (para autocomplete)."""
    nomes = sorted([chave.title() for chave in MEDICAMENTOS.keys()])
    return jsonify({"medicamentos": nomes, "total": len(nomes)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
