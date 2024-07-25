function deleteFile(filename) {
    if (confirm("Tem certeza que deseja excluir este arquivo?")) {
        fetch(`/delete/${filename}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Arquivo excluído: " + filename);
                
                location.reload();
            } else {
                alert("Erro ao excluir o arquivo.");
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
            alert("Erro ao excluir o arquivo.");
        });
    }
}

function checkFile() {
        const fileInput = document.getElementById('fileInput');
        const errorMessage = document.getElementById('error-message');

        errorMessage.textContent = '';

        if (fileInput.files.length === 0) {
            errorMessage.textContent = "Por favor, selecione um arquivo.";
            return false; 
        }

        return true; 
    }