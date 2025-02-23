const Environnement = () => {
    const environnement = import.meta.env.VITE_ENVIRONNEMENT || "local"
    return <div>
        Environnement de déploiement : {environnement}
    </div>
}

export default Environnement;