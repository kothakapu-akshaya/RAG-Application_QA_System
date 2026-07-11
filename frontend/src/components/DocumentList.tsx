type Document = {
  id: string;
  name: string;
};

type DocumentListProps = {
  documents: Document[];
  onDelete: (id: string) => void;
};

function DocumentList({ documents, onDelete }: DocumentListProps) {
  return (
    <section>
      <h2>Uploaded Documents</h2>

      {documents.length === 0 ? (
        <p>No documents uploaded yet.</p>
      ) : (
        <ul className="document-list">
          {documents.map((doc) => (
            <li key={doc.id} className="document-item">
              <span>{doc.name}</span>

              <button onClick={() => onDelete(doc.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default DocumentList;
